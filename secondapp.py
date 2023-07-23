from fastapi import FastAPI, HTTPException
import requests

app = FastAPI()

@app.get("/numbers")
async def get_numbers(urls: list[str]):
    merged_numbers = []

    for url in urls:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                numbers = data.get("numbers")
                merged_numbers.extend(numbers)
        except requests.exceptions.Timeout:
            # Handle timeout for remote URLs
            continue
        except Exception:
            # Handle other exceptions
            continue

    merged_numbers = sorted(list(set(merged_numbers)))

    return {"numbers": merged_numbers}