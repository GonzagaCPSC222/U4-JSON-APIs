# @author Gina Sprint
# Get Distance and Duration Between Two Addresses
# Use Google Maps Distance Matrix API: https://developers.google.com/maps/documentation/distance-matrix/start
# Great example of API key in url query params
# Note: to make an API key for this API requires a billing account (hence why we did the free (no billing account required) MapQuest demo instead)

import requests
import json

# TODO: move these into a file/environment variable external to the code
API_KEY = "YOUR API KEY HERE"

url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
url += "key=" + API_KEY
# note: if value has special characters like , in it, use requests.utils.quote() to encode
url += "&origins=Spokane"
url += "&destinations=Seattle"
url += "&units=imperial"
# print(url) # NOTE: printing url shows key
    
response = requests.get(url=url)
json_object = json.loads(response.text)
print(json_object)

rows_array = json_object["rows"]
first_row_object = rows_array[0]
elements_object = first_row_object["elements"]

first_element_object = elements_object[0]
distance_object = first_element_object["distance"]
miles_str = distance_object["text"]
print(miles_str, "from Spokane to Seattle")

# task: get duration text
duration_object = first_element_object["duration"]
duration_str = duration_object["text"]
print(duration_str, "from Spokane to Seattle")

# output:
# {'destination_addresses': ['Seattle, WA, USA'], 'origin_addresses': ['Spokane, WA, USA'], 'rows': [{'elements': [{'distance': {'text': '279 mi', 'value': 448517}, 'duration': {'text': '4 hours 16 mins', 'value': 15370}, 'status': 'OK'}]}], 'status': 'OK'}
# 279 mi from Spokane to Seattle
# 4 hours 16 mins from Spokane to Seattle