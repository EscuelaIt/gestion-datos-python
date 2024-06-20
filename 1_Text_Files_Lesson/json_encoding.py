import json

json_dict = {'name': 'Almudena', 'age': 9}
json_list = ['18122014', {'name': 'Mayra', 'age': 37}]

print(type(json_dict))
print(type(json_list))

json_object = json.dumps(json_dict)
json_array = json.dumps(json_list)

print(type(json_object))
print(type(json_array))

# Write to a file

json_file = open('data.json', 'w')
json_file.writelines(json_array)
json_file.close()
