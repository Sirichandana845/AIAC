import requests
import json

def get_weather(city):
    # OpenWeatherMap API endpoint and API key
    api_key = "3fbce54d73d27b5fbeef6838857b5741"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # For temperature in Celsius
    }
    
    # Make API request
    response = requests.get(base_url, params=params)
    
    # Get the JSON data
    weather_data = response.json()
    
    # Print formatted JSON output
    print(json.dumps(weather_data, indent=2))

# Example usage
if __name__ == "__main__":
    city_name = "London"  # Example city
    get_weather(city_name)