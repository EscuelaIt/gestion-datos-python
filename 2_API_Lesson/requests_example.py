import requests

url = 'https://imgs.xkcd.com/comics/python.png'

response = requests.get(url)

'''
print(type(response))

print(dir(response))

print(response.request)
print(response.status_code)
print(response.headers)
'''

image_bytes = response.content

with open('image.png', 'wb') as image_file:
    image_file.write(image_bytes)
