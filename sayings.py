def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")

# main will not get called if we are importing the file, let's say because we want to
# use those defined functions in a different code
if __name__ == "__main__":
    main()

# if the name of this directory is the same as name of the directory, where it's called, run main
