import requests
res = requests.get('https://www.linkedin.com/feed/')
with open('html.txt' , 'w') as file:
    file.write(res.text)
# print(res.text)
