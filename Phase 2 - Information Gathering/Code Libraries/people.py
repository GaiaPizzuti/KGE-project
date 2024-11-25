import requests
import json

link = "https://webapps.unitn.it/api/du/v1/persona/search?text=&filter=&items=100"

people = {}

for i in range(1, 52):
    response = requests.get(link + "&page=" + str(i), timeout=5)
    json_data = response.json()
    for person in json_data['data']:
        people[person["nominativo"]] = person["email"]

with open ('../UniTN/people_emails.json', 'w') as f:
    json.dump(people, f, indent=4, ensure_ascii=False)
