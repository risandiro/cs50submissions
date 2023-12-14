import sys

def main():
    input_check()



def input_check():
    if len(sys.argv) == 3:
        if sys.argv[1].endswith([".jpg", ".jpeg", ".png"]):
            if sys.argv[2].endswith([".jpg", ".jpeg", ".png"]):
                _, ext1 = sys.argv[1].split(".")
                _, ext2 = sys.argv[2].split(".")
                if ext1 == ext2:
                    return



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
