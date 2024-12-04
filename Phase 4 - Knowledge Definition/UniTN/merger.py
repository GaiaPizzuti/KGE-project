import json

with open("DU-UNITN-people.json") as f:
    people = json.load(f)

with open("people_emails.json") as f:
    emails = json.load(f)

for person in people["value"]["data"]:
    full_name = person["name"]
    if "surname" in person:
        full_name = person["name"] + " " + person["surname"]
    if full_name in emails:
        person["email"] = emails[full_name]
    else:
        print("No email found for", full_name)

with open("DU-UNITN-people.json", "w") as f:
    json.dump(people, f, indent=4)