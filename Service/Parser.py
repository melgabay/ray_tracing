
from typing import List
from Models.Vector3D import Vector3
from Models.Scene import Scene
from Models.Material import Material
from Models.Objects.Sphere import Sphere
from Models.Objects.Plane import Plane
from Models.Lights.AmbientLight import AmbientLight
from Models.Lights.DirectionalLight import DirectionalLight
from Models.Lights.SpotLight import SpotLight

def parse_file(path: str) -> Scene:
    """Parse the scene description file and return Scene object."""
    with open(path, "r") as f:
        lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]

    # We'll parse in two passes; first get eye and ambient
    eye = Vector3(0,0,5)
    ambient_col = Vector3(0,0,0)
    objects_data = []
    materials_data = []
    lights_temp = []
    spot_positions = []
    spot_cutoffs = []

    for line in lines:
        parts = line.split()
        tag = parts[0]
        vals = list(map(float, parts[1:]))
        if tag == "e":
            eye = Vector3(*vals[:3])
        elif tag == "a":
            ambient_col = Vector3(*vals[:3])
        elif tag == "o":
            objects_data.append(vals)  # store for later
        elif tag == "c":
            materials_data.append(vals)
        elif tag == "d":
            # directional or spotlight direction
            dir_vec = Vector3(*vals[:3])
            is_spot = abs(vals[3]-1.0) < 1e-3
            lights_temp.append(("dir", dir_vec, is_spot))
        elif tag == "p":
            pos = Vector3(*vals[:3])
            cutoff_cos = vals[3]
            spot_positions.append((pos, cutoff_cos))
        elif tag == "i":
            color = Vector3(*vals[:3])
            # temporarily append color; association later
            lights_temp.append(("intensity", color))
        else:
            print(f"Unknown tag {tag}")

    scene = Scene(eye, ambient_col)
    scene.add_light(AmbientLight(ambient_col))

    # Build objects with materials matching order
    for obj_vals, mat_vals in zip(objects_data, materials_data):
        mat = Material(
            ambient=Vector3(*mat_vals[:3]),
            diffuse=Vector3(*mat_vals[:3]),
            shininess=mat_vals[3]
        )
        if obj_vals[3] > 0:  # sphere
            center = Vector3(*obj_vals[:3])
            radius = obj_vals[3]
            scene.add_object(Sphere(center, radius, mat))
        else:  # plane
            normal = Vector3(*obj_vals[:3])
            d = obj_vals[3]
            scene.add_object(Plane(normal, d, mat))

    # Build lights
    intensity_queue: List[Vector3] = []
    for entry in lights_temp:
        if entry[0] == "intensity":
            intensity_queue.append(entry[1])
    intensity_idx = 0
    spot_idx = 0
    for entry in lights_temp:
        if entry[0] == "dir":
            direction, is_spot = entry[1], entry[2]
            color = intensity_queue[intensity_idx] if intensity_idx < len(intensity_queue) else Vector3(1,1,1)
            intensity_idx += 1
            if is_spot:
                pos, cutoff_cos = spot_positions[spot_idx]
                spot_idx += 1
                scene.add_light(SpotLight(pos, direction, cutoff_cos, color))
            else:
                scene.add_light(DirectionalLight(direction, color))
        # intensity entries already consumed

    return scene
