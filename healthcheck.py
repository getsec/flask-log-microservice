from requests import get

url = "http://localhost:80/log/pub"

try:
    r = get(url)
    if not r.ok:
        print(f"Error, Non-200 Code {r.status_code}")

except Exception as msg:
    print("Error connecting to endpoint.")
    print(f"exception: {msg}")

