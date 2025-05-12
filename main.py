
#!/usr/bin/env python
import sys, os
from Models.Vector3D import Vector3
from Service.Parser import parse_file
from Service.RayCaster import render
from Handler.ScreenHandler import save_image

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <scene.txt> [output.png]")
        sys.exit(1)
    scene_file = sys.argv[1]
    output = sys.argv[2] if len(sys.argv) > 2 else "output.png"

    scene = parse_file(scene_file)
    img = render(scene, width=400, height=400)
    save_image(img, output)
    print(f"Rendered {output}")

if __name__ == "__main__":
    main()
