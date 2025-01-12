import requests

FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

API_KEY = "8d8fb6c28e3e4ac9848182006251201"
BASE_URL = "http://api.weatherapi.com/v1/current.json?"

def get_weather(city_name):
    url = f"{BASE_URL}key={API_KEY}&q={city_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current']['temp_c']
        description = data['current']['condition']['text'] 
        print(f"The current temperature in {city_name} is {temperature}°C with {description}.")
        return temperature
    else:
        print("City not found or an error occurred.")
        return None

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)

def convert_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

def main():
    city = input("Enter the name of the city to get the weather: ")
    temperature = get_weather(city)
    if temperature is not None:
        unit = input("Would you like to convert this temperature to Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'F':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp}°F")
        elif unit == 'C':
            print(f"The temperature is already in Celsius: {temperature}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")
    else:
        print("Temperature conversion could not be done due to an error.")

if __name__ == "__main__":
    main()
    