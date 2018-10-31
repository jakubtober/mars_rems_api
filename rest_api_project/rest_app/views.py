from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from rest_framework import generics
from rest_app.models import Sol
from rest_app.serializers import SolSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# Create your views here.


class WelcomeView(View):
    def get(self, request):
        return HttpResponse('Hello citizens of Earth!')


class SolCreateView(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Sol.objects.all()
    serializer_class = SolSerializer


class SolListAPIView(generics.ListAPIView):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer


class SolDetailView(generics.RetrieveAPIView):
    queryset = Sol.objects.all()
    serializer_class = SolSerializer
    lookup_field = 'sol'


class SolUpdateView(generics.UpdateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Sol.objects.all()
    serializer_class = SolSerializer
    lookup_field = 'sol'


class SolDeleteView(generics.DestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    queryset = Sol.objects.all()
    serializer_class = SolSerializer
    lookup_field = 'sol'
