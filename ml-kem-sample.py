import requests
response = requests.get("https://kyber.club/api?algo=ml-kem-512")
keys = response.json()
print("Public Key:", keys["public_key"])
print("Private Key:", keys["private_key"])
# Source: https://kyber.club/api-docs
