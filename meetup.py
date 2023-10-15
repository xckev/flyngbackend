import requests
import os
from dotenv import load_dotenv
load_dotenv()
flightkey = os.getenv("flightkey")

params = {
  'access_key': flightkey,
  'dep_iata': 'SEA',
  'limit': 50
}

api_result = requests.get('http://api.aviationstack.com/v1/flights?access_key='+flightkey, params)
api_response = api_result.json()
'''
api_response = {
  "pagination": {
    "limit": 100,
    "offset": 0,
    "count": 100,
    "total": 1669022
  },
  "data": [
    {
      "flight_date": "2019-12-12",
      "flight_status": "active",
      "departure": {
        "airport": "San Francisco International",
        "timezone": "America/Los_Angeles",
        "iata": "SFO",
        "icao": "KSFO",
        "terminal": "2",
        "gate": "D11",
        "delay": 13,
        "scheduled": "2019-12-12T04:20:00+00:00",
        "estimated": "2019-12-12T04:20:00+00:00",
        "actual": "2019-12-12T04:20:13+00:00",
        "estimated_runway": "2019-12-12T04:20:13+00:00",
        "actual_runway": "2019-12-12T04:20:13+00:00"
      },
      "arrival": {
        "airport": "Dallas/Fort Worth International",
        "timezone": "America/Chicago",
        "iata": "DFW",
        "icao": "KDFW",
        "terminal": "A",
        "gate": "A22",
        "baggage": "A17",
        "delay": 0,
        "scheduled": "2019-12-12T04:20:00+00:00",
        "estimated": "2019-12-12T04:20:00+00:00",
        "actual": None,
        "estimated_runway": None,
        "actual_runway": None
      },
      "airline": {
        "name": "American Airlines",
        "iata": "AA",
        "icao": "AAL"
      },
      "flight": {
        "number": "1004",
        "iata": "AA1004",
        "icao": "AAL1004",
        "codeshared": None
      },
      "aircraft": {
        "registration": "N160AN",
        "iata": "A321",
        "icao": "A321",
        "icao24": "A0F1BB"
      },
      "live": {
        "updated": "2019-12-12T10:00:00+00:00",
        "latitude": 36.28560000,
        "longitude": -106.80700000,
        "altitude": 8846.820,
        "direction": 114.340,
        "speed_horizontal": 894.348,
        "speed_vertical": 1.188,
        "is_ground": None
      }
    }, 
    {
      "flight_date": "2020-11-10",
      "flight_status": "scheduled",
      "departure": {
        "airport": "Seattle-Tacoma International Airport",
        "timezone": "America/Los_Angeles",
        "iata": "SEA",
        "icao": "KSFO",
        "terminal": "2",
        "gate": "D11",
        "delay": 13,
        "scheduled": "2019-12-12T04:20:00+00:00",
        "estimated": "2019-12-12T04:20:00+00:00",
        "actual": "2019-12-12T04:20:13+00:00",
        "estimated_runway": "2019-12-12T04:20:13+00:00",
        "actual_runway": "2019-12-12T04:20:13+00:00"
      },
      "arrival": {
        "airport": "John F. Kennedy International Airport",
        "timezone": "America/New_York",
        "iata": "JFK",
        "icao": "KDFW",
        "terminal": "A",
        "gate": "A22",
        "baggage": "A17",
        "delay": 0,
        "scheduled": "2019-12-12T04:20:00+00:00",
        "estimated": "2019-12-12T04:20:00+00:00",
        "actual": None,
        "estimated_runway": None,
        "actual_runway": None
      },
      "airline": {
        "name": "American Airlines",
        "iata": "AA",
        "icao": "AAL"
      },
      "flight": {
        "number": "1004",
        "iata": "AA1004",
        "icao": "AAL1004",
        "codeshared": None
      },
      "aircraft": {
        "registration": "N160AN",
        "iata": "A321",
        "icao": "A321",
        "icao24": "A0F1BB"
      },
      "live": {
        "updated": "2019-12-12T10:00:00+00:00",
        "latitude": 36.28560000,
        "longitude": -106.80700000,
        "altitude": 8846.820,
        "direction": 114.340,
        "speed_horizontal": 894.348,
        "speed_vertical": 1.188,
        "is_ground": None
      }
    }
  ]
}'''
print(len(api_response['data']))
for f in api_response['data']:
  print(f['flight']['iata'], "departed from gate", f['departure']['gate'], "of", f['departure']['iata'], "to", f['arrival']['gate'], "of", f['arrival']['iata'], "at scheduled time", f['departure']['scheduled'])