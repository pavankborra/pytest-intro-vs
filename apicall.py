import requests
import os

BASE_URL = "https://api.zippopotam.us/us/"

# zipcode = input("Enter a zipcode: ")
zipcode = "66614"
requests_url = f"{BASE_URL}{zipcode}"
response = requests.get(requests_url)

# This can be used to test the api call or uncomment this to see how the info below gets pulled from the API
# data = response.json()
# print(data)

if response.status_code == 200:
    data = response.json()
    country = data['country']
    place_name = data['places'][0]['place name']    
    state_name = data['places'][0]['state']    
    state_code = data['places'][0]['state abbreviation']  
    
    print("Country:", country)
    print("State:", state_name)
    print("State Code:", state_code)
    print("Place name:", place_name)
else:
    print("An error occurred.")