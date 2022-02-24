import requests 
import json 

url = "https://opentdb.com/api.php?amount=5&category=15&difficulty=easy"

# make an HTTP GET request using the above URL
response = requests.get(url)
json_str = response.text 
# print(json_str)
json_obj = json.loads(json_str)
results_list = json_obj["results"]
# print(results_list)
for results_obj in results_list:
    # task: grab the question and print it out
    # print(results_obj)
    question = results_obj["question"]
    # challenge task: extract the answers
    # correct and incorrect 
    # prompt the user for their choice
    # and score their answer
    print(question)
    print() 