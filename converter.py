from PIL import Image

LIST_BLOCK = [152, 2, 57, 173]
RGB_COLOR = [(255, 0, 0), (0, 128, 0), (0, 0, 255), (0, 0, 0)]


def convert_png_to_code(image, y):
    img = Image.open(image)
    output = ["import mc;from mc import world\n"]
    for x in range(img.size[0]):
        for z in range(img.size[1]):
            if img.getpixel((x, z)) != (255, 255, 255):
                for _ in range(4):
                    if img.getpixel((x, z)) == RGB_COLOR[_]:
                        output.append(f"world.setBlock({x-63},{y},{z-63},{LIST_BLOCK[_]})\n")

    return output


def testPillow():
    try:
        Image.new('RGB', (126, 126), color=(255, 255, 255))
        return "Pillow installed"

    except: return "Pillow not installed/not working"


if __name__ == "__main__":
    print(testPillow())
