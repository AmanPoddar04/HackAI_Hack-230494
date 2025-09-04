from uagents import Model

# Define a model for weather requests
class WeatherRequest(Model):
    # Latitude of the location for the weather request
    latitude: float
    # Longitude of the location for the weather request
    longitude: float
