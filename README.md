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

## Example data entry for single sol:

{
    "sol": 2213,
    "earths_date": "2018-10-27",
    "air_temp_max": -12,
    "air_temp_min": -70,
    "ground_temp_max": 6,
    "ground_temp_min": -71,
    "pressure": 874,
    "wind_speed": "Value not available",
    "humidity": "Value not available",
    "sunrise_time": "06:11:00",
    "sunset_time": "18:29:00",
    "atmospheric_opacity": "Sunny",
    "radiation_level": "UV Radiation level moderated"
}

## sol data description:

* "sol" - day of the mission represented in sol (Mars day: the duration of this day-and-night cycle on Mars (one day) is 24 hours, 39 minutes and 35.244 seconds on Earth.)
* "earths_date" - date on Earth when data was collected
* "air_temp_max" - measured in Celsius degrees
* "air_temp_min" - measured in Celsius degrees
* "ground_temp_max" - measured in Celsius degrees
* "ground_temp_min" - measured in Celsius degrees
* "pressure" - measured in Pa
* "wind_speed" - measured in Km/h
* "humidity" - measured in %
* "sunrise_time" - time of sunrise
* "sunset_time" - time of sunset
* "atmospheric_opacity" - atmospheric visibility (e.g. sunny)
* "radiation_level" - level of radiation (e.g. low, moderate, severe)
