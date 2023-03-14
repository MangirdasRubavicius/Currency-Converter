from datetime import date
today_date = date.today()
yuan_conversion = 0.15
yuan_conversion = float(yuan_conversion)
usd_conversion = 6.85
usd_conversion = float(usd_conversion)
if __name__ == "__main__":
    currency_choice = input("Please input which currency you are going to convert: Yuan or USD.")
    if currency_choice == "USD":
        currency_amount = input("Please input the amount of USD you are going to convert.")
        currency_amount = float(currency_amount)
        converted_currency = currency_amount // yuan_conversion
        print("Today is :", today_date, " 1 USD yields 6.85 Chinese Yuan. " " Converting from USD to Yuan yielded :", converted_currency , " yuan.")
    elif currency_choice == "Yuan":
        currency_amount = input("Please input the amount of Yuan you are going to convert.")
        currency_amount = float(currency_amount)
        converted_currency = currency_amount // usd_conversion
        print("Today is :", today_date, " 1 Yuan yields 0,15 USD. " " Converting from Yuan to USD yielded :", converted_currency, " USD.")
    else:
        print("Command not recognized")