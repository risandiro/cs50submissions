import sys, requests

if len(sys.argv) == 1:
    print("Missing command-line argument")

elif len(sys.argv) == 2:
    try:
        nmbr = float(sys.argv[1])
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = response.json()
        x = response["bpi"]
        x = x["USD"]
        x = x["rate_float"]
        result = float(x * nmbr)
        print(f"${result:,.4f}")

    except ValueError:
        sys.exit("Command-line argument is not a number")

    except requests.RequestException:
        pass
