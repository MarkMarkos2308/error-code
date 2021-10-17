import requests
import os

# # problem 1
#
# r = 'http://httpbin.org/#/Auth/get_basic_auth__user___passwd_'
# r = requests.get(r)
# print(r.text)
# print(r.content)

# # problem 2
#
# r = 'https://httpbin.org/'
# d = {"name": "Bob", "age": "25"}
# r = requests.get(r, params=d)
# print(r.url)
# print(r.text)

# # problem 3
#
# r = 'http://httpbin.org/#/Auth/get_basic_auth__user___passwd_'
# d = {"name": "Mark", "password": "1234567890"}
# r = requests.post(r, data=d)
# print(r.url)
# # tyragir@ indz sa tvec
# sa = {
#   "authenticated": True,
#   "user": "Mark"
# }

# # problem 4
#
# ls = ['https://www.istockphoto.com/stock-photos/nature-and-landscapes', 'https://www.istockphoto.com/stock-photos/jobs-and-careers', 'https://www.istockphoto.com/stock-photos/lifestyle', 'https://www.istockphoto.com/stock-photos/holidays-and-seasonal']
# # os.mkdir("pr4_basic")
# for i in range(len(ls)):
#     file = "file" + str(i) + '.png'
#     with open(file, "wb") as f:
#         for y in ls:
#             l = requests.get(y).content
#             f.write(l)
#         f.close()
