import requests

from urllib.parse import urlparse, parse_qs

url_string = "http://localhost:3000/numbers?url=http://20.244.56.144/numbers/primes&url=http://abc.com/fibo&url=http://localhost:3000/numbers"

parsed_url = urlparse(url_string)

urls = parse_qs(parsed_url.query).get('url', [])

print(urls)