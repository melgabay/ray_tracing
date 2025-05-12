# Ray Tracing – Python Project

This project implements a basic ray tracing engine in Python. It generates an image by simulating how light rays travel and interact with objects in a 3D scene.

## Objectives

The main goal is to build a rendering engine that can:

- Handle geometric objects like spheres and planes.
- Simulate various types of lights (ambient, directional, spot).
- Apply lighting effects (diffuse, specular).
- Describe a scene using a text file.
- Generate a final image using ray tracing from a virtual camera.

## Project Structure

The project is organized into several modules:

- `Models/Vector3D.py`: basic 3D vector operations.
- `Models/Objects/`: geometric objects (Sphere, Plane, etc.).
- `Models/Lights/`: different types of light sources.
- `Models/Scene.py`: manages the scene (objects + lights).
- `Service/RayCaster.py`: the ray tracing engine.
- `Service/Parser.py`: parses scene description files.
- `Handler/ScreenHandler.py`: creates and saves the output image.
- `main.py`: the main entry point of the program.

## How to Run

```bash
python main.py scene_demo.txt output.png
```

This command loads the scene from `scene_demo.txt` and generates the image `output.png`.

## Scene File Format

A scene file is a simple text file describing the camera, lights, and objects. Example:

```
camera: 0 0 -5
light: ambient 0.2 0.2 0.2
light: directional 1 1 -1 0.8 0.8 0.8
object: sphere 0 0 0 1 1 0 0 0.6 0.6 0.6 100
```

Each line defines either the camera, a light source, or an object.

## Output

The program generates a `.png` image with pixel colors calculated based on ray-object intersections and lighting.
