import requests
import json
from pprint import pprint

myCity = input("What is your city? ")
FoodChoice = input("What would you like to search for? ")

API_key = 'Your API Key'
client_id = 'F1oAG49WJt-yVXvdyKnU7w'
ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
HEADERS = {'Authorization': 'Bearer %s' % API_key}

PARAMETERS = {
	'term' : FoodChoice,
	'limit' : 10,
	'location' : myCity,
	'radius' : 10000
}

response = requests.get(url = ENDPOINT, params = PARAMETERS, headers = HEADERS)
data = response.json()


for place in data['businesses']:
	print(place['name'])
	print(place['location']['display_address'])
