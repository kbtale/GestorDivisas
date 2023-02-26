from django.http import HttpResponse
from django.template import Template, Context
from GestorDivisas.services import callAPI
import datetime


# First view
def welcome(request):  # A request object is the first argument
    return HttpResponse('Welcome')


def showdata(request):
    data = callAPI('https://s3.amazonaws.com/dolartoday/data.json')
    tmpFile = open("D:\Programming\Code\Python\GestorDivisas\GestorDivisas\mainpage.html")
    dataTemplate = Template(tmpFile.read())
    tmpFile.close()
    dt = datetime.datetime.now().strftime("%A, %d/%m/%Y, %I:%M:%S")
    ctx = Context({"USD_BCV": data["USD"]["sicad2"],
                    "USD_DT": data["USD"]["dolartoday"],
                    "USD_LB": data["USD"]["localbitcoin_ref"],
                    "EUR_BCV": data["EUR"]["sicad2"],
                    "EUR_DT": data["EUR"]["dolartoday"],
                    "EUR_LB": data["EUR"]["sicad1"],
                    "DT": dt
                    })
    document = dataTemplate.render(ctx)
    return HttpResponse(document)
