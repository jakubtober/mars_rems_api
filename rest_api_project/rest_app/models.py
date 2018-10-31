from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

# "10": {
#   "ground_temp_max": "8",
#   "earths_date": "2012-08-16",
#   "sol": "10",
#   "pressure": "739",
#   "air_temp_max": "-16",
#   "sunrise_time": "05:28",
#   "air_temp_min": "-75",
#   "radiation_level": "UV Radiation level very high",
#   "wind_speed": "Value not available",
#   "atmospheric_opacity": "Sunny",
#   "ground_temp_min": "-83",
#   "sunset_time": "17:22",
#   "humidity": "Value not available"
# },

# self.last_day_data = {
#     'earths_date': browser.find_element_by_id('mw-terrestrial_date').text,
#     'sol': browser.find_element_by_id('mw-sol').text,
#     'air_temp_min': browser.find_element_by_id('mw-min_temp').text,
#     'air_temp_max': browser.find_element_by_id('mw-max_temp').text,
#     'ground_temp_min': browser.find_element_by_id('mw-min_gts_temp').text,
#     'ground_temp_max': browser.find_element_by_id('mw-max_gts_temp').text,
#     'pressure': browser.find_element_by_id('mw-pressure').text,
#     'wind_speed': browser.find_element_by_id('mw-wind_speed').text,
#     'humidity': browser.find_element_by_id('mw-abs_humidity').text,
#     'sunrise_time': browser.find_element_by_id('mw-sunrise').text,
#     'sunset_time': browser.find_element_by_id('mw-sunset').text,
#     'atmospheric_opacity': browser.find_element_by_id('mw-atmo_opacity').text,
#     'radiation_level': (
#         browser.find_element_by_id('mw-local_uv_irradiance_index')
#         .find_element_by_tag_name('span')
#         .get_attribute('title')
#     ),


class Sol(models.Model):
    sol = models.IntegerField()
    earths_date = models.DateField()
    air_temp_max = models.IntegerField()
    air_temp_min = models.IntegerField()
    ground_temp_max = models.IntegerField()
    ground_temp_min = models.IntegerField()
    pressure = models.IntegerField()
    wind_speed = models.CharField(max_length=64)
    humidity = models.CharField(max_length=64)
    sunrise_time = models.TimeField()
    sunset_time = models.TimeField()
    atmospheric_opacity = models.CharField(max_length=64)
    radiation_level = models.CharField(max_length=128)

    def __str__(self):
        return str("Sol: " + self.sol)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
