import json

d = {
    'url': 'https://escuela.it',
    'name': 'Escuela IT',
    'version': 1,
    'is_responsive': True,
    'account': None,
    'list': [1, 2, 3]
}

data = json.dumps(d)
#print(type(data))
#print(data)

dict = json.loads(data)
#print(type(dict))
#print(dict)

d = json.loads('[null, true, false, "string", 1, 2, 0]')
print(d)
