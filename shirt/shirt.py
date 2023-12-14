import sys, os, Pillow

def main():
    input_check()





def input_check():
    ext = [".jpg", ".jpeg", "png"]
    if len(sys.argv) == 3:
        if sys.argv[1].endswith(tuple(ext)):
            if sys.argv[2].endswith(tuple(ext)):
                _, ext1 = sys.argv[1].split(".")
                _, ext2 = sys.argv[2].split(".")
                if ext1 == ext2:
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
