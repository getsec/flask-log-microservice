from requests import get

url = "http://localhost:80/log/pub"

try:
    get(url)
except Exception as msg:
    print("Error connecting to endpoint.")
    print(f"exception: {msg}")

