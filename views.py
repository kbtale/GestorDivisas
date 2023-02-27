from django.http import HttpResponse
from django.template import Template, Context
from django.template.defaulttags import register
from GestorDivisas.services import callAPI
import datetime


# First view
def welcome(request):  # A request object is the first argument
    return HttpResponse('Welcome')


def showdata(request):
    sources = ["Banco Central de Venezuela", "DolarToday", "LocalBitcoin"]
    data = callAPI('https://s3.amazonaws.com/dolartoday/data.json')
    tmpFile = open("D:\Programming\Code\Python\GestorDivisas\GestorDivisas\mainpage.html")
    dataTemplate = Template(tmpFile.read())
    tmpFile.close()
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
            "sources": [
                {
                    "name": sources[0],
                    "value": data["USD"]["sicad2"]
                },
                {
                    "name": sources[1],
                    "value": data["USD"]["dolartoday"]
                },
                {
                    "name": sources[2],
                    "value": data["USD"]["localbitcoin_ref"]
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
            "sources": [
                {
                    "name": sources[0],
                    "value": data["EUR"]["sicad2"]
                },
                {
                    "name": sources[1],
                    "value": data["EUR"]["dolartoday"]
                },
                {
                    "name": sources[2],
                    "value": data["EUR"]["sicad1"]
                }
            ]
        },
    ]
    ctx = Context({"currencies": currencies, "DT": dt})
    document = dataTemplate.render(ctx)
    return HttpResponse(document)


