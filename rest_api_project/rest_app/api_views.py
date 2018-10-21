from rest_framework import viewsets
from rest_app import models, serializers


class SolViewset(viewsets.ModelViewSet):
    queryset = models.Sol.objects.all()
    serializer_class = serializers.SolSerializer
