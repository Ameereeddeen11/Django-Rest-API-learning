import requests

endpoint = "http://127.0.0.1:8000/api/"
get_response = requests.get(endpoint) #HTTP request 
print(get_response.json()["message"]) #print raw text response