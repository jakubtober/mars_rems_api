from rest_framework import routers
from rest_app import api_views as myapp_views

router = routers.DefaultRouter()
router.register(r'sols', myapp_views.SolViewset)
