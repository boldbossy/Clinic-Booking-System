from flask import Flask, jsonify
from flask_cors import CORS 
import os
from invokes import invoke_http
app = Flask(__name__)
CORS(app) 

@app.route("/searching/<string:loc>", methods=['GET'])
def searchByLoc(loc):
    key = "8e365c1c857ef28683f96abda3b5b5e2f88c1b69cea158dcb1ca04f63b423ec9"
    results = invoke_http("https://serpapi.com/search.json?engine=google&q=Clinics&location="+loc+"&google_domain=google.com.sg&gl=sg&hl=en&api_key="+key, method='GET')
    results = results.get("local_results").get("places")
    clinicdict = {}
    for i in range(len(results)):
        clinicdict[i] = results[i]
    return jsonify(
        {
        "code": 201,
        "data": {
            "clinic_result": clinicdict
        }
    }
    )

#Execute this program if it is run as a main script (not by 'import')
if __name__ == "__main__":
    print("This is flask " + os.path.basename(__file__) +
          " for placing an order...")
    app.run(host="0.0.0.0", port=5100, debug=True)
    # Notes for the parameters:
    # - debug=True will reload the program automatically if a change is detected;
    #   -- it in fact starts two instances of the same flask program,
    #       and uses one of the instances to monitor the program changes;
    # - host="0.0.0.0" allows the flask program to accept requests sent from any IP/host (in addition to localhost),
    #   -- i.e., it gives permissions to hosts with any IP to access the flask program,
    #   -- as long as the hosts can already reach the machine running the flask program along the network;
    #   -- it doesn't mean to use http://0.0.0.0 to access the flask program.


