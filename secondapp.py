from fastapi import FastAPI, HTTPException
import requests

from urllib.parse import urlparse, parse_qs
app = FastAPI()

@app.post("/numbers")
async def get_numbers(URL_string: str):
    merged_numbers = []
    # print(urls)

    #urls = ['http://localhost:3000/numbers', 'http://20.244.56.144/numbers/primes', 'http://abc.com/fibo']


    parsed_url = urlparse(URL_string)
    urls = parse_qs(parsed_url.query).get('url', [])
    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                numbers = data.get("numbers")
                merged_numbers.extend(numbers)
        except requests.exceptions.Timeout:
            
            continue
        except Exception:
            
            continue

    merged_numbers = sorted(list(set(merged_numbers)))

    return {"numbers": merged_numbers}