from PIL import Image
from PIL import ImageOps
import sys
import os

def main():
    print(creating_image())

def check_commandline():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    argv_one, argv_two = sys.argv[1], sys.argv[2]

    if not (argv_one.endswith(".png") or argv_one.endswith(".jpeg") or argv_one.endswith(".jpg")):
        sys.exit("Invalid input")
    elif not (argv_two.endswith(".jpeg") or argv_two.endswith(".png") or argv_two.endswith(".jpg")):
        sys.exit("Invalid output")

    ext_one = os.path.splitext(argv_one)[-1]
    ext_two = os.path.splitext(argv_two)[-1]

    if ext_one != ext_two:
        sys.exit("Input and output have different extensions")

def creating_image():
    check_commandline()

    try:
        shirt = Image.open("shirt.png")
        image = Image.open(sys.argv[1])

        resized_image = ImageOps.fit(image, shirt.size)
        resized_image.paste(shirt, shirt)
        resized_image.save(sys.argv[2])

    except FileNotFoundError:
        sys.exit("Input does not exist")

    return "ok"

if __name__ == "__main__":
    main()
