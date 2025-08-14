import csv
import os
from statistics import mean

class WeatherLogger:
    def __init__(self, filename="weather_data.csv"):
        self.filename = filename
        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Temperature", "Humidity"])

    def log_data(self, date, temperature, humidity):
        with open(self.filename, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, temperature, humidity])
        print(f" Data logged for {date}")

    def read_data(self):
        with open(self.filename, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)

    def show_stats(self):
        data = self.read_data()
        if not data:
            print("No data available.")
            return
        temperatures = [float(row["Temperature"]) for row in data]
        humidities = [float(row["Humidity"]) for row in data]
        print(f"Avg Temp: {mean(temperatures):.2f}°C, Min Temp: {min(temperatures)}°C, Max Temp: {max(temperatures)}°C")
        print(f" Avg Humidity: {mean(humidities):.2f}%, Min Humidity: {min(humidities)}%, Max Humidity: {max(humidities)}%")

logger = WeatherLogger()
logger.log_data("2025-08-14", 32.5, 70)
logger.log_data("2025-08-15", 29.8, 65)
logger.show_stats()
