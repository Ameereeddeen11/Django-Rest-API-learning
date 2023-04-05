import requests

endpoint = "https://httpbin.org/anything"
get_response = requests.get(endpoint) #HTTP request 
print(get_response.json()) #print raw text response