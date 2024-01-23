import sys
import requests


def main():
    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")


def btc_price(num):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        dolar_price = result["bpi"]["USD"]["rate_float"]
        eur_price = result['bpi']['EUR']['rate_float']
        dolar_total = dolar_price * num
        eur_total = eur_price * num

        return f"${dolar_total:,.2f}\n€{eur_total:,.2f}"
    
    except requests.RequestException:
        return None


main()
