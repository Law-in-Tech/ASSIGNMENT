import requests

# Function to fetch weather data
def get_weather(city, api_key):
    """
    Fetch weather data for the specified city using the OpenWeatherMap API.

    :param city: City name
    :param api_key: Your OpenWeatherMap API key
    :return: Weather details as a dictionary
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Use metric units for temperature in Celsius
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
    return None

# Function to display weather details
def display_weather(data):
    """
    Display weather details in a readable format.

    :param data: Weather data dictionary
    """
    if not data:
        print("No weather data to display.")
        return

    city = data.get("name")
    country = data["sys"].get("country")
    weather_desc = data["weather"][0].get("description").capitalize()
    temp = data["main"].get("temp")
    feels_like = data["main"].get("feels_like")
    humidity = data["main"].get("humidity")
    wind_speed = data["wind"].get("speed")

    print(f"\nWeather in {city}, {country}:")
    print(f"Description: {weather_desc}")
    print(f"Temperature: {temp}°C (Feels like {feels_like}°C)")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")

# Main program
if __name__ == "__main__":
    print("=== Weather Application ===")
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    city = input("Enter the name of the city: ")

    # Fetch weather data
    weather_data = get_weather(city, api_key)

    # Display the weather information
    if weather_data and weather_data.get("cod") == 200:
        display_weather(weather_data)
    else:
        print("City not found or error retrieving data.")
