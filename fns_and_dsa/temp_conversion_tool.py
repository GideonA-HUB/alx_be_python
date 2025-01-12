import requests

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

API_KEY = "316ad5e6aca7ea97ec1ad9d8668c0d34"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    url = f"{BASE_URL}q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        print(f"The current temperature in {city_name} is {temperature}°C.")
        return temperature
    else:
        print("City not found or an error occurred.")
        return None

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    city = input("Enter the name of the city to get the weather: ")
    temperature = get_weather(city)
    if temperature is not None:
        unit = input("Would you like to convert this temperature to Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'F':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'C':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°C is {converted_temp}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")
    else:
        print("Temperature conversion could not be done due to an error.")

if __name__ == "__main__":
    main()
