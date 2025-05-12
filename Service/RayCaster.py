
import numpy as np
from Models.Vector3D import Vector3
from Models.Objects.Ray import Ray
from Models.Scene import Scene
from Models.Lights.DirectionalLight import DirectionalLight
from Models.Lights.SpotLight import SpotLight
from Models.Lights.AmbientLight import AmbientLight

MAX_DEPTH = 1
BACKGROUND = Vector3(0,0,0)
BIAS = 1e-4
CHECKER_SIZE = 1.0

def checkerboard_modifier(point: Vector3) -> float:
    # simple checker on XZ
    if ((int((point.x + 1000)/CHECKER_SIZE) + int((point.z + 1000)/CHECKER_SIZE)) % 2) == 0:
        return 1.0
    else:
        return 0.5

def trace_ray(ray: Ray, scene: Scene, depth: int=0):
    if depth > MAX_DEPTH:
        return BACKGROUND

    hit_t = float("inf")
    hit_info = None
    for obj in scene.objects:
        res = obj.intersect(ray)
        if res and res[0] < hit_t:
            hit_t, hit_point, hit_normal, hit_mat = res
            hit_info = (hit_point, hit_normal, hit_mat)

    if hit_info is None:
        return BACKGROUND

    point, normal, mat = hit_info
    view_dir = (-ray.direction).normalize()
    color = scene.ambient * mat.ambient  # global ambient

    # Checkerboard diffuse mod for planes
    diffuse_mod = 1.0
    specular_mod = 1.0
    if hasattr(mat, "_is_plane") or any(isinstance(obj, type(hit_info)) for obj in []):
        pass
    # We simply use checker modifier if object is Plane by property attached in Plane intersect
    if hasattr(mat, "checker") and mat.checker:
        diffuse_mod = checkerboard_modifier(point)

    for light in scene.lights:
        if isinstance(light, AmbientLight):
            continue
        if isinstance(light, DirectionalLight):
            L = (-light.direction).normalize()  # vector from point to light
            light_dist = float("inf")  # infinite
        elif isinstance(light, SpotLight):
            L = (light.position - point)
            if not light.inside_cone(-L):  # inside cone check expects (light->point) opposite maybe adjust
                continue
            light_dist = L.norm()
            L = L.normalize()
        else:
            continue

        # Shadow ray
        shadow_origin = point + normal * BIAS
        shadow_ray = Ray(shadow_origin, L)
        in_shadow = False
        for obj in scene.objects:
            res_shadow = obj.intersect(shadow_ray)
            if res_shadow:
                t_shadow = res_shadow[0]
                if t_shadow < light_dist - BIAS:
                    in_shadow = True
                    break
        if in_shadow:
            continue

        # Diffuse
        diff_intensity = max(0.0, normal.dot(L))
        diffuse = mat.diffuse * diff_intensity * diffuse_mod

        # Specular
        half = (L + view_dir).normalize()
        spec_intensity = max(0.0, normal.dot(half)) ** mat.shininess
        specular = mat.specular * spec_intensity

        color += (diffuse + specular) * light.color

    # Clamp
    color = Vector3(min(color.x,1.0), min(color.y,1.0), min(color.z,1.0))
    return color

def render(scene: Scene, width: int=400, height: int=400) -> np.ndarray:
    aspect = width / height
    img = np.zeros((height, width, 3), dtype=np.uint8)

    for j in range(height):
        y = 1 - 2 * (j + 0.5) / height  # top=1 bottom=-1
        for i in range(width):
            x = 2 * (i + 0.5) / width - 1  # left=-1 right=1
            x *= aspect
            pixel_point = Vector3(x, y, 0)
            ray_dir = (pixel_point - scene.eye).normalize()
            ray = Ray(scene.eye, ray_dir)
            col = trace_ray(ray, scene)
            img[j, i] = (np.array(col.to_tuple()) * 255).astype(np.uint8)
    return img
