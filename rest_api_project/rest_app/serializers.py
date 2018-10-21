from rest_framework import serializers
from rest_app.models import Sol

class SolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sol
        fields = (
            'sol',
            'earths_date',
            'air_temp_max',
            'air_temp_min',
            'ground_temp_max',
            'ground_temp_min',
            'pressure',
            'wind_speed',
            'humidity',
            'sunrise_time',
            'sunset_time',
            'atmospheric_opacity',
            'radiation_level',
        )
