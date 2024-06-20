import json

poke_json = json.load(open('poke.json'))

print(type(poke_json))
print(poke_json['forms'][0]['name'])
