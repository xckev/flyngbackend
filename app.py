import requests
import google.generativeai as palm
from flask import Flask, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
apikey = os.getenv("apikey")
flightkey = os.getenv("flightkey")
print(apikey)
palm.configure(api_key=apikey)


@app.route('/api/<string:flightnum>', methods=['GET'])
def get_people(flightnum):
  '''
  params = {
  'access_key': flightkey,
  'flight_iata': flightnum,
  'limit': 1
  }'''
  #api_result = requests.get('http://api.aviationstack.com/v1/flights', params)
  #api_response = jsonify(api_result)
  #print(api_response)

  #gate = api_response['departure']['gate']

  people = requests.get("https://us-west1-festive-airway-393617.cloudfunctions.net/getgateusers")
  #print(people["body"]["0"])
  #toReturn = jsonify(people)
  #toReturn.headers.add('Access-Control-Allow-Origin', '*')
  return str(people)

@app.route('/gates/<string:gate1>/<string:gate2>', methods=['GET'])
def get_meet_info(gate1, gate2):
  response = palm.generate_text(prompt="Name a few good shops, restaurants, or gates for socializing in between gate {} and gate {} inside of SeaTac airport".format(gate1, gate2))
  #print( "Flight Number: {} ".format(flightnum))
  #print(response.result)
  toReturn = jsonify({"text": response.result})
  toReturn.headers.add('Access-Control-Allow-Origin', '*')
  return toReturn
'''
@app.route('/api/<string:gate1>/<string:gate2>', methods=['GET'])
def get_meet_info(gate1, gate2):
  response = palm.generate_text(prompt="Name a few good shops, restaurants, or gates for socializing in between gate {} and gate {} inside of SeaTac airport".format(gate1, gate2))
  #print( "Flight Number: {} ".format(flightnum))
  #print(response.result)
  return jsonify({"text": response.result})
'''
if(__name__ == "__main__"):
  #parser = argparse.ArgumentParser()
  #-flightnum
  #parser.add_argument("-flight", "--flightnum", help="Flight Number", required=True)
  #args = parser.parse_args()
  
  app.run(debug=True)
