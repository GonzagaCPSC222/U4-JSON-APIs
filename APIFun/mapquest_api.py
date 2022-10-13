import requests
import json

# storing your API key in code
# like what we just did
# is considered "bad practice"
# you should never share your API key
# with anyone or make it publicly available
api_key = "YOUR API KEY HERE"

url = "http://www.mapquestapi.com/directions/v2/route"
url += "?key=" + api_key
url += "&from=spokane&to=seattle"
print(url)

# task: print out the route distance and time
response = requests.get(url=url)
print(response.text)
json_obj = json.loads(response.text)
route_obj = json_obj["route"]
print(route_obj["distance"])
print(route_obj["formattedTime"])