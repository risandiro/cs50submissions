import sys, requests

if len(sys.argv) == 1:
    print("Missing command-line argument")

if len(sys.argv) == 2:
    try:
        nmbr = float(sys.argv[1])
    except ValueError:
        print("Command-line argument is not a number")
