import requests
import time

def get_iss_location():
    try:
        response = requests.get("http://api.open-notify.org/iss-now.json")
        data = response.json()
        latitude = float(data["iss_position"]["latitude"])
        longitude = float(data["iss_position"]["longitude"])
        return latitude, longitude
    except requests.RequestException as e:
        print(f"Error fetching ISS location: {e}")
        return None

def get_country_from_coords(latitude, longitude, api_key):
    try:
        url = f"https://api.opencagedata.com/geocode/v1/json?key={api_key}&q={latitude}+{longitude}&pretty=1"
        response = requests.get(url)
        data = response.json()
        components = data.get("results", [])[0].get("components", {})
        country = components.get("country", "Unknown, probably over the ocean")
        return country
    except requests.RequestException as e:
        print(f"Error fetching country information: {e}")
        return "Unknown, probably in space"

def start():
    api_key = "20c295d9597a4bc68f39c387e4e5090b"  # OpenCage API key
    location = get_iss_location()
    if location:
        latitude, longitude = location
        country = get_country_from_coords(latitude, longitude, api_key)
        return (f"The ISS is currently above: {country}")
 
if __name__ == "__main__":
    country = start()
    print (country)