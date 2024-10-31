import sys
import requests
import logging
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel,
                             QLineEdit, QPushButton, QVBoxLayout)
from PyQt5.QtCore import Qt

# Set up logging configuration for detailed tracking
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
API_KEY = 'YOUR_API_KEY'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        logging.info("Initializing WeatherApp UI components.")

        # Initialize UI components
        self.city_label = QLabel("Enter city name:", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel("Temperature: N/A", self)
        self.emoji_label = QLabel("🌞", self)
        self.description_label = QLabel("Description: N/A", self)

        logging.info("UI components initialized successfully.")
        self.initUI()

    def initUI(self):
        # Set up the main window title
        self.setWindowTitle("Weather App")
        logging.debug("Setting window title to 'Weather App'.")

        # Set up the layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)

        # Center-align labels and button
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        logging.debug("Layout and alignment configured.")

        # Connect the button to the function to fetch weather
        self.get_weather_button.clicked.connect(self.fetch_weather)
        logging.info("Button connected to fetch_weather function.")

        # Apply styles
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: Calibri;
            }
            QLabel#city_label {
                font-size: 14px;
            }
        """)
        logging.info("Stylesheet applied successfully.")

    def fetch_weather(self):
        # Get city name from the input field
        city = self.city_input.text()
        if not city:
            logging.warning("City input is empty.")
            self.description_label.setText("Please enter a city name.")
            return
        logging.info(f"City entered: {city}")

        # Set up parameters for the API request
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }

        logging.info(f"Fetching weather data for city: {city}")

        try:
            # Make the request to the weather API
            response = requests.get(BASE_URL, params=params)
            response.raise_for_status()
            data = response.json()
            logging.debug(f"API response data: {data}")

            # Extract relevant data
            temp = data['main']['temp']
            description = data['weather'][0]['description']
            icon = data['weather'][0]['icon']

            # Update labels
            logging.info("Updating UI labels with weather data.")
            self.temperature_label.setText(f"Temperature: {temp}°C")
            self.description_label.setText(f"Description: {description.capitalize()}")
            self.emoji_label.setText(self.get_weather_emoji(icon))

            logging.info(f"Weather data displayed for {city}: {temp}°C, {description.capitalize()}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching weather data: {e}")
            self.description_label.setText("Could not retrieve weather data.")
            logging.debug(f"Failed API request with parameters: {params}")
        except KeyError as e:
            logging.error(f"Key error when parsing weather data: {e}")
            self.description_label.setText("Error in weather data format.")
            logging.debug(f"Data received that caused KeyError: {data}")

    def get_weather_emoji(self, icon_code):
        # Basic mapping of OpenWeatherMap icons to emojis
        logging.debug(f"Mapping weather icon code to emoji: {icon_code}")
        if icon_code.startswith("01"):
            return "☀️"  # Clear sky
        elif icon_code.startswith("02") or icon_code.startswith("03") or icon_code.startswith("04"):
            return "☁️"  # Cloudy
        elif icon_code.startswith("09") or icon_code.startswith("10"):
            return "🌧️"  # Rain
        elif icon_code.startswith("11"):
            return "⛈️"  # Thunderstorm
        elif icon_code.startswith("13"):
            return "❄️"  # Snow
        elif icon_code.startswith("50"):
            return "🌫️"  # Mist
        else:
            return "🌡️"  # Unknown

if __name__ == "__main__":
    # Start the application
    logging.info("Starting the WeatherApp application.")
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    logging.info("WeatherApp window shown.")
    
    # Execute the app loop
    sys.exit(app.exec_())
