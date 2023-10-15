import argparse
import google.generativeai as palm
from flask import Flask, jsonify
import os

app = Flask(__name__)
apikey = "AIzaSyCB6Lbog3oBWQvTkumuhILNdQMatJAjHWo"
palm.configure(api_key=apikey)

@app.route('/api/people', methods=['GET'])
def get_items():
  return jsonify({"testfield": 69})

if(__name__ == "__main__"):
  parser = argparse.ArgumentParser()
  #-flightnum
  parser.add_argument("-flight", "--flightnum", help="Flight Number", required=True)
  args = parser.parse_args()

  response = palm.generate_text(prompt="Give me information about flight {}".format(args.flightnum))
  print( "Flight Number: {} ".format(
    args.flightnum
  ))
  print(response.result)
  
  app.run(host="0.0.0.0", port=8000, debug=True)
