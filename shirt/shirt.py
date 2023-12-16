import sys, os
from PIL import Image

def main():
    input_check()
    try:
        shirt = Image.open("shirt.png")
        size = shirt.size

        image = Image.open(sys.argv[1])
        PIL.ImageOps.fit(image, size)
        image.paste(image, shirt)



    except FileNotFoundError:
        sys.exit("Input does not exist")


def input_check():
    ext = [".jpg", ".jpeg", "png"]
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(tuple(ext)):
            if sys.argv[2].endswith(tuple(ext)):
                root_ext1 = os.path.splitext(sys.argv[1])
                root_ext2 = os.path.splitext(sys.argv[2])
                if root_ext1[1] == root_ext2[1]:
                    return

                else:
                    sys.exit("Input and output have different extensions")
            else:
                sys.exit("Invalid output")
        else:
            sys.exit("Invalid input")
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
