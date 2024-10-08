import base64
import json
import requests
from datetime import datetime
from app.models import Payment
from dotenv import load_dotenv
import os

load_dotenv()

def generate_access_token():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')

    
    encoded_credentials = base64.b64decode(f'{consumer_key}:{consumer_secret}'.encode())
    
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate"
    querystring = {"grant_type":"client_credentials"}
    payload = ""
    headers = {
            "Authorization": f"Basic {encoded_credentials}"
        }
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    return response.text   


def lipanampesa():
    token = generate_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortCode = "9276285"
    passkey = os.getenv('PASSKEY')
    url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
    stk_password = base64.b64encode((shortCode + passkey + timestamp).encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer' + token,
        'Content-Type': 'application/json'
        }
    requestBody = {
        "BusinessShortCode": shortCode,
        "Password": stk_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerBuyGoodsOnline",
        "Amount": 1,
        "PartyA": 254741644151,
        "PartyB": shortCode,
        "PhoneNumber": 254741644151,
        "CallbackURL": '',
        "Transactiondesc": 'Test'
        }
    
    try:
        response = requests.post(url, json=requestBody, headers=headers)
        print(response.json())
        return response.json()
    
    except Exception as e:
        print(f'Error: {str(e)}')

def lipanafamilybank():
    token = generate_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortCode = '222111'
    passkey = os.getenv('PASSKEY')
    url = ''
    stk_password = base64.b64encode((shortCode + passkey + timestamp).encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer' + token,
        'Content-Type': 'application/json'
        }
    
    requestBody = {
        "BusinessShortCode": shortCode,
        "BillRefNumber": '752292',
        "Password": stk_password,
        "TransactionType": "CustomerPaybillonline",
        "Amount": 1,
        "PartyA": 254741644151,
        "PartyB": shortCode,
        "CallbackURL": '',
        "Transactiondesc": 'Test'
        }
    
    try:
        response = requests.post(url, json=requestBody, headers=headers)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f'Error: {str(e)}')

def lipanacoop():
    token = generate_access_token()
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    shortCode = '400200'
    passkey = os.getenv('PASSKEY')
    url = ''
    stk_password = base64.b64encode((shortCode + passkey +timestamp).encode('utf-8')).decode('utf-8')

    headers = {
        'Authorization': 'Bearer' + token,
        'Content-Type': 'application/json'
        }
    
    requestBody = {
        "BusinessShortCode": shortCode,
        "BillRefNumber": '37681',
        "Passwword": stk_password,
        "TransactionType": "CustomerPaybillOnline",
        "Amount": 1,
        "PartyA": 254741644151,
        "PartyB": shortCode,
        "CallbackURL": '',
        "Transactiondesc": "Test"
        }
    
    try:
        response = requests.post(url, json=requestBody, headers=headers)
        return response.json()
    except Exception as e:
        print(f'Error: {str(e)}')