import json

voters_details = {'Emeka': 'Duru'}
registered_voters = []
path = 'text_files/voters.json'

with open(path, 'r') as voters:
    json.dump(voters_details, voters)
