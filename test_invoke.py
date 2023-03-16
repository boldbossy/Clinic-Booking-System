# test_invoke_http.py
import json
from invokes import invoke_http

# invoke book microservice to get all books
loc="Jurong East"
results = invoke_http("https://serpapi.com/search.json?engine=google&q=Clinics&location="+loc+"&google_domain=google.com.sg&gl=sg&hl=en&api_key=8e365c1c857ef28683f96abda3b5b5e2f88c1b69cea158dcb1ca04f63b423ec9", method='GET')
results = results.get("local_results").get("places")
clinicdict = {}
for i in range(len(results)):
    clinicdict[i] = results[i]

print(type(clinicdict) )
#print()
print(clinicdict)