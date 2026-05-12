from django.shortcuts import render
from django.http import HttpResponse
from GestorDivisas.services import callAPI
import datetime


# First view
def welcome(request):  # A request object is the first argument
    return HttpResponse('Welcome')


def showdata(request):
    sources = ["Banco Central de Venezuela", "DolarToday", "LocalBitcoins"]
    data = callAPI('https://s3.amazonaws.com/dolartoday/data.json')
    offline = False

    # Validate API response structure; fall back to reference demo data if API fails or changes format
    try:
        if not data or not isinstance(data, dict) or "USD" not in data or "EUR" not in data:
            raise ValueError("API returned empty/invalid response")
        # Ensure nested keys exist as well
        for cur in ["USD", "EUR"]:
            for key in ["sicad2", "dolartoday"]:
                if key not in data[cur]:
                    raise ValueError(f"Missing key {key} in {cur}")
            if cur == "USD" and "localbitcoin_ref" not in data[cur]:
                raise ValueError("Missing localbitcoin_ref in USD")
            if cur == "EUR" and "sicad1" not in data[cur]:
                raise ValueError("Missing sicad1 in EUR")
    except Exception:
        offline = True
        data = {
            "USD": {
                "sicad2": "36.25",
                "dolartoday": "43.50",
                "localbitcoin_ref": "41.90"
            },
            "EUR": {
                "sicad2": "39.10",
                "dolartoday": "47.20",
                "sicad1": "45.80"
            }
        }

    dt = datetime.datetime.now().strftime("%A, %d/%m/%Y, %I:%M:%S")
    currencies = [
        {
            "name": "USD",
            "icon": """
                    <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-coin" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
                       <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                       <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
                       <path d="M14.8 9a2 2 0 0 0 -1.8 -1h-2a2 2 0 1 0 0 4h2a2 2 0 1 1 0 4h-2a2 2 0 0 1 -1.8 -1"></path>
                       <path d="M12 7v10"></path>
                    </svg>""",
            "symbol": "&#36;",
            "sources": [
                {
                    "name": sources[0],
                    "value": data["USD"]["sicad2"],
                    "icon": 'https://svgshare.com/i/qgC.svg'
                },
                {
                    "name": sources[1],
                    "value": data["USD"]["dolartoday"],
                    "icon": 'https://svgshare.com/i/qfv.svg'
                },
                {
                    "name": sources[2],
                    "value": data["USD"]["localbitcoin_ref"],
                    "icon": 'https://svgshare.com/i/qgD.svg'
                }
            ]
        },
        {
            "name": "EUR",
            "icon": """
            <svg xmlns="http://www.w3.org/2000/svg" class="icon icon-tabler icon-tabler-coin-euro" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round">
               <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
               <path d="M12 12m-9 0a9 9 0 1 0 18 0a9 9 0 1 0 -18 0"></path>
               <path d="M14.401 8c-.669 -.628 -1.5 -1 -2.401 -1c-2.21 0 -4 2.239 -4 5s1.79 5 4 5c.9 0 1.731 -.372 2.4 -1"></path>
               <path d="M7 10.5h4"></path>
               <path d="M7 13.5h4"></path>
            </svg>
            """,
            "symbol": "&#8364;",
            "sources": [
                {
                    "name": sources[0],
                    "value": data["EUR"]["sicad2"],
                    "icon": 'https://svgshare.com/i/qgC.svg'
                },
                {
                    "name": sources[1],
                    "value": data["EUR"]["dolartoday"],
                    "icon": 'https://svgshare.com/i/qfv.svg'
                },
                {
                    "name": sources[2],
                    "value": data["EUR"]["sicad1"],
                    "icon": 'https://svgshare.com/i/qgD.svg'
                }
            ]
        },
    ]
    return render(request, 'mainpage.html', {"currencies": currencies, "DT": dt, "offline": offline})



