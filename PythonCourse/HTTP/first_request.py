import requests

# res = requests.get("https://news.ycombinator.com/")
# print(res)  # Response [200]
# print(res.ok)  # True
# print(res.headers)  # Hrpa Koda
# print(res.text)  # Printa HTML
url = "https://www.google.com"
response = requests.get(url)

print(
    f"your request for {url} came back with status code: {response.status_code}")
