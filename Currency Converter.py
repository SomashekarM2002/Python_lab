import requests

def convert_currency(amount, from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    response = requests.get(url)

    if response.status_code != 200:
        print("Error fetching exchange rates.")
        return

    data = response.json()
    rates = data["rates"]

    if to_currency.upper() not in rates:
        print(f"Currency '{to_currency}' not supported.")
        return

    converted_amount = amount * rates[to_currency.upper()]
    print(f"{amount} {from_currency.upper()} = {converted_amount:.2f} {to_currency.upper()}")

# Example usage:
amount = float(input("Enter amount: "))
from_currency = input("From currency (e.g., USD): ")
to_currency = input("To currency (e.g., INR): ")

convert_currency(amount, from_currency, to_currency)
