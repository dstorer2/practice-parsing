import requests
import json
from date import *

def test_api_call():
    url = "http://worldclockapi.com/api/json/est/now"

    headers = {'Content-Type': 'application/json' } 

    # Body
    payload = {'key1': 1, 'key2': 'value2'}
    
    # convert dict to json string by json.dumps() for body data. 
    resp = requests.get(url).json()
    # responseData = {
    #     '$id': '1',
    #     'currentDateTime': '2022-01-06T12:14-05:00',
    #     'utcOffset': '-05:00:00',
    #     'isDayLightSavingsTime': False,
    #     'dayOfTheWeek': 'Thursday',
    #     'timeZoneName': 'Eastern Standard Time',
    #     'currentFileTime': 132859448869139983,
    #     'ordinalDate': '2022-6',
    #     'serviceResponse': None
    # }

    currentDateTime = '2022-01-06T12:14-05:00'

    
    # Validate response headers and body contents, e.g. status code.
    # assert resp.status_code == 200
    # resp_body = resp.json()
    # assert resp_body['url'] == url
    
    # print response full body as text
    print(resp.json())

test_api_call()
