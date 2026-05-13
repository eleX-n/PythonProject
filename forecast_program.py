import requests
import json
import os
from datetime import datetime, timedelta

CACHE_FILE = "weather_cache.json"

LATITUDE = 52.2298
LONGITUDE = 21.0118

API_URL = "https://api.open-meteo.com/v1/forecast"


class WeatherForecast:
    def __init__(self):
        self.cache = self.load_cache()

    # ----- CACHE -----
    def load_cache(self):
        if os.path.exists(CACHE_FILE):
            try:
                with open(CACHE_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return {}
        return {}

    def save_cache(self):
        with open(CACHE_FILE, "w") as file:
            json.dump(self.cache, file, indent=2)

    # ----- API -----
    def fetch_precipitation(self, date):
        url = (
            f"{API_URL}?latitude={LATITUDE}&longitude={LONGITUDE}"
            f"&daily=precipitation_sum"
            f"&timezone=Europe/London"
            f"&start_date={date}&end_date={date}"
        )

        try:
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                return None

            data = response.json()
            return data["daily"]["precipitation_sum"][0]

        except:
            return None

    # ----- DUNDER METHODS -----
    def __getitem__(self, date):
        if date in self.cache:
            print("(Using cached data)")
            return self.cache[date]

        print("Fetching from API...")
        precipitation = self.fetch_precipitation(date)

        self.cache[date] = precipitation
        self.save_cache()

        return precipitation

    def __setitem__(self, date, value):
        self.cache[date] = value
        self.save_cache()

    def __iter__(self):
        return iter(self.cache.keys())

    # ----- ITEMS GENERATOR -----
    def items(self):
        for date, value in self.cache.items():
            yield (date, value)


# ----- MAIN PROGRAM -----
def main():
    weather_forecast = WeatherForecast()

    date = input("Enter date (YYYY-MM-DD) or press Enter: ").strip()

    if not date:
        date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

    precipitation = weather_forecast[date]

    print(f"\nWeather on {date}:")

    if precipitation is None or precipitation < 0:
        print("I don't know")
    elif precipitation == 0.0:
        print("It will not rain")
    else:
        print(f"It will rain ({precipitation} mm)")

    print("\nSaved forecasts:")
    for d, p in weather_forecast.items():
        print(d, "->", p)


# ----- RUN -----
if __name__ == "__main__":
    main()