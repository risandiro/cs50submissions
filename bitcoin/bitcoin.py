import sys, requests

if len(sys.argv) == 1:
    print("Missing command-line argument")

if len(sys.argv) == 2:
    try:
        nmbr = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()


    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestsException:
        pass
