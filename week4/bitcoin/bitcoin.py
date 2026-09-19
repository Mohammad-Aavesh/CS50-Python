import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)
    try:
        float(sys.argv[1])
    except ValueError:
        print("Command-line arguement is not a number")
        sys.exit(1)

    api_k = "30b07c5c0829d130b0581cb093f6c1eefefa151f0456f731fc0a6714a2937ab7"
    url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_k}"

    try:
        response = requests.get(url)
        data = response.json()
        bitcoin_Value = float(data["data"]['priceUsd']) * float(sys.argv[1])
        bitcoin_Value = f"${bitcoin_Value:,.4f}"
        print(bitcoin_Value)
    except requests.RequestException:
        sys.exit(1)

if __name__ == "__main__":
    main()
