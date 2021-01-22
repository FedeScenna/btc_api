import requests
from django.shortcuts import render

def home(request):
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    all_data = response.json()
    btc_price = "$ " + all_data["bpi"]["USD"]["rate"]
    return render(request, "btc_api/home.html", {"price": btc_price})
