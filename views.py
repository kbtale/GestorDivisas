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


