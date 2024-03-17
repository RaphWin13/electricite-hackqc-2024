import requests
import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_GEOCODE_API_URL = f"https://maps.googleapis.com/maps/api/geocode/json?key={os.getenv('GOOGLE_GEOCODE_API_KEY')}&address="

def convert_to_lat_long(address: str, region:str, country: str = "CA") -> dict[str, float]:
    url = GOOGLE_GEOCODE_API_URL + address + ",+" + region + ",+" + country
    response = requests.get(url)

    if response.status_code == 200:
        resp_json_payload = response.json()

        if 'results' in resp_json_payload and len(resp_json_payload['results']) > 0: 
            position = resp_json_payload['results'][0]['geometry']['location']
            return position
        else:
            raise Exception("Address not converted to lat long. No results found.")
        
    else:
        raise Exception("Error while trying to convert address to lat long")