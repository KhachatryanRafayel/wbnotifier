from datetime import datetime
import requests

def get_exchange_rate(from_currency, to_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    response = requests.get(url)
    data = response.json()
    return data['rates'][to_currency]

def format_datetime(notformatted):
    dt = datetime.strptime(notformatted, "%Y-%m-%dT%H:%M:%SZ")
    formatted = dt.strftime("%d.%m.%y at %H:%M")
    return formatted

def get_country_name_by_code(currencycode):
    currency_country_map = {    
    '643': 'Russia',
    '398': 'Kazakhstan', 
    '933': 'Belarus',
    '417': 'Kyrgyzstan',
    '51': 'Armenia',
    '944': 'Azerbaijan',
    '860': 'Uzbekistan',
    '972': 'Tajikistan',
    '498': 'Moldova',
    '980': 'Ukraine',
    '981': 'Georgia'
    }
    return currency_country_map.get(str(currencycode), 'unknown')