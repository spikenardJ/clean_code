# Question 1: Refactoring a Weather Forecast Application into Classes and Modules

# Task 1: Identifying and Creating Classes

# Simulated data based on city


class WeatherDataFetcher: # Simulated function to fetch weather data for a given city
    def __init__(self):
        self.weather_data = {
            "New York": {"Temperature": 70, "Condition": "Sunny 🌞", "Humidity": 50, "City": "New York"},
            "London": {"Temperature": 60, "Condition": "Cloudy ⛅️", "Humidity": 65, "City": "London"},
            "Tokyo": {"Temperature": 75, "Condition": "Rainy ⛈️", "Humidity": 70, "City": "Tokyo"}
        }

    def fetch_weather_data(self, city):
       return self.weather_data.get(city, {}) 

class DataParser: # Function to parse weather data
    def __init__(self):
        pass

    def parse_weather_data(self, data):
        if not data:
            return "Weather data not available."
        city = data["City"]
        temperature = data["Temperature"]
        condition = data["Condition"]
        humidity = data["Humidity"]
        return f"Weather in {city}: {temperature} Degrees, Condition: {condition}, Humidity: {humidity}%"

class UserInterface:
    def __init__(self, weather_data_fetcher, data_parser):
        self.weather_data_fetcher = weather_data_fetcher
        self.data_parser = data_parser

    def get_detailed_forecast(self, city): # Function to provide a detailed weather forecast for a city
        data = self.weather_data_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city): # Function to display the basic weather forecast for a city
        data = self.weather_data_fetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}.")
        else:
            weather_report = self.data_parser.parse_weather_data(data)
            print(weather_report)

def main():
    weather_data_fetcher = WeatherDataFetcher()
    data_parser = DataParser()
    user_interface = UserInterface(weather_data_fetcher, data_parser)
    while True:
        try:
            city = input("\nEnter the 'City' to get it's weather forecast or 'Exit' to quit: ").title()
            if city.title() == "Exit":
                print("\nGoodbye 👋\n")
                break
            detailed_forecast = input(f"Do you want a detailed forecast of {city}? (Yes / No): ").title()
            forecast = ""
            if detailed_forecast == "Yes":
                forecast = user_interface.get_detailed_forecast(city)
            else:
                forecast = user_interface.display_weather(city)
            print("\n", forecast)
        except Exception as e:
            print(f"An error occured: {e}")

if __name__ == "__main__":
    main()