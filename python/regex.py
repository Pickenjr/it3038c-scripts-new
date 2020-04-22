import requests, re
data = "Hello. My email is pickenjr@mail.uc.edu. Please do not contact me!"
p = re.compile('[A-Za-z0-9_%.-]+@[A-z0-9]{2,}')
print(p.search(data).group())