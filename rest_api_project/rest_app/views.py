from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import generics
from rest_app.models import Sol
from rest_app.serializers import SolSerializer

# Create your views here.

class WelcomeView(View):
    def get(self, request):
        return HttpResponse('Hello citizens of Earth!')

class SolListAPIView(generics.ListAPIView):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer
