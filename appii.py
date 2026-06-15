# from urllib.request import Request, urlopen
# #module             library         function
# #obj  class   constructor
# req = Request(url='https://jsonplaceholder.typicode.com/posts',method='GET')
# #api call done -|
# response = urlopen(req)
# print(response.read())
# # req1 = Request(url='https://jsonplaceholder.typicode.com/posts/88',method='GET')
# # response1= urlopen(req1)
# # print(response1.read())
# #above in python

import requests
res = requests.get('https://jsonplaceholder.typicode.com/posts/88')
print(res)
#response 200 -> OK
#response 401 -> unauthorised
#response 404 -> Not found [route directory wrong]
# response 500 -> backend server down
print(res.__dict__) #all data
print(res.status_code)
print(res.elapsed) #time
print(res.headers) 
for key in res.headers.items(): #clean way
    print(key) 
print(res.cookies)
print(res._content)