import json

filetoimport = "example.json"
with open('example.json','r') as json_data:
    users = json.load(json_data)
    for user in users:
        print(user['firstname'] + " " + user['lastname'])
        for pet in user['pets']:
            print pet