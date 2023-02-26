import requests
import logging

def generateRequest(url, params={}):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()

def callAPI(APIurl,params={}):
    try:
        response = generateRequest(APIurl, params)
        if response:
            return response
    except:
        logging.WARNING("Fetch models from {APIurl} failed")

    return ''