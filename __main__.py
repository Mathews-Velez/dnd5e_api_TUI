import requests

#the url being used to make the api request
URL = "https://www.dnd5eapi.co/api/monsters"

#reciving a param for the api request
CR = input("Please enter the the challenge rating you wish your monster to have: ")

PARAMS = {'challenge_rating':CR}

r = requests.get(url = URL, params = PARAMS)
data = r.json()

print("Got %s results back"%data['count'])

#iterate through each result and display it's name
for i in data['results']:
    print(f"{data['results'].index(i)} ---"+i['name'])

