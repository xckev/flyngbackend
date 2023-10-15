#import argparse
import google.generativeai as palm
from flask import Flask, jsonify
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
apikey = os.getenv("apikey")
print(apikey)
palm.configure(api_key=apikey)

@app.route('/api/<string:flightnum>', methods=['GET'])
def get_items(flightnum):
  response = palm.generate_text(prompt="Give me information about flight {}".format(flightnum))
  print( "Flight Number: {} ".format(
    flightnum
  ))
  print(response.result)
  return jsonify({"testfield": response.result})

if(__name__ == "__main__"):
  #parser = argparse.ArgumentParser()
  #-flightnum
  #parser.add_argument("-flight", "--flightnum", help="Flight Number", required=True)
  #args = parser.parse_args()

  
  
  app.run(debug=True)
