# MARS REMS Data - REST API

REST API created using Django Rest Framework - CRUD for Mars REMS data (will be used by MartianUpdates twitter bot).

API uses TokenAuthentication, CREATE, UPDATE and DELETE views require user authentication

## API endpoints

* /api/sols/
* /api/sols/sol_number/
* /api/token-auth/
* /api/sols/create/ - authentication is required
* /api/sols/sol_number/update/ - authentication is required
* /api/sols/sol_number/delete/ - authentication is required

## Single sol data:

* "sol": 2213 - day of the mission represented in sol (Mars day: the duration of this day-and-night cycle on Mars (one day) is 24 hours, 39 minutes and 35.244 seconds on Earth.)
* "earths_date": "2018-10-27"
* "air_temp_max": -12 - measured in Celsius degrees
* "air_temp_min": -70 - measured in Celsius degrees
* "ground_temp_max": 6 - measured in Celsius degrees
* "ground_temp_min": -71 - measured in Celsius degrees
* "pressure": 874 - measured in Pa
* "wind_speed": "Value not available" - measured in Km/h
* "humidity": "Value not available" - measured in %
* "sunrise_time": "06:11:00"
* "sunset_time": "18:29:00"
* "atmospheric_opacity": "Sunny"
* "radiation_level": "UV Radiation level moderated"
