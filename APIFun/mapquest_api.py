import requests 
import json 

api_key = "YOUR API KEY HERE"

url = "http://www.mapquestapi.com/directions/v2/route"
url += "?key=" + api_key
url += "&from=spokane&to=seattle"

print(url)
response = requests.get(url)
json_str = response.text 
print(json_str)
json_obj = json.loads(json_str)
route_obj = json_obj["route"]
# print("****", route_obj)
distance = route_obj["distance"]
formattedTime = route_obj["formattedTime"]
print(distance)
print(formattedTime)