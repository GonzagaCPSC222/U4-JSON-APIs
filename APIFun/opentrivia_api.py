import requests
import json
import html

url = "https://opentdb.com/api.php?amount=5&category=9&difficulty=easy"

# make a GET request for data
response = requests.get(url=url)
# print(response.text)
json_obj = json.loads(response.text)
print(type(json_obj))
# task: print out each question
# challenge task: prompt the user for a guess and check
# their answer
results_list = json_obj["results"]
for result_obj in results_list:
    question = result_obj["question"]
    question = html.unescape(question)
    print(question)
    print()