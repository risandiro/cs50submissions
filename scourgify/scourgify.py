import sys, csv

def main():
    cma_check()
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            with open(sys.argv[2], "w") as file_0:
                writer = csv.DictWriter(file_0, fieldnames=["first name", "last name", "house"])
                writer.writeheader()

                for row in reader:
                    last_name, first_name = row["name"].strip().split(",")
                    with open(sys.argv[2], "a") as file_1:
                            writer.writerow({"first name": first_name, "last name": last_name, "house": row["house"]})

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")





def cma_check():
    if len(sys.argv) == 3:
        return
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")


if __name__ == "__main__":
    main()
