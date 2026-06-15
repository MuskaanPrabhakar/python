####POST CREATION 
# import requests
# res = requests.post(url='https://jsonplaceholder.typicode.com/posts', data= {"title":"test", "body":"test body", "userId": 999})
# print(res.json()) #creating post

#always wrap above so that if route is wrong, server down or any problem posts to create
# import requests
# try:
#     res = requests.post(url='https://jsonplaceholder.typicode.com/posts', data= {"title":"test", "body":"test body", "userId": 999})
#     print(res.json())
#     res.raise_for_status()
# except Exception as e:
#     print(e)

####PARAMS CONCEPT to get data
# import requests
# try:
#     res = requests.get('https://jsonplaceholder.typicode.com/posts', params= {"userId":1})
#     print(res.json())
#     res.raise_for_status()
# except Exception as e:
#     print(e)

####put data to update
# import requests
# try:
#     res = requests.put('https://jsonplaceholder.typicode.com/posts/1', data= {'id' :1 ,"title":"test", "body":"test body", "userId": 999})
#     print(res.json())
#     res.raise_for_status()
# except Exception as e:
#     print(e)

####patch: partial updates to an existing resource
import requests
try:
    res = requests.patch('https://jsonplaceholder.typicode.com/posts/1', data= {"title":"test"})
    print(res.json())
    res.raise_for_status()
except Exception as e:
    print(e)