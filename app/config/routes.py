from rest_framework import routers
from core.viewsets import CoreViewSet


router = routers.SimpleRouter()
router.register(r"", CoreViewSet, basename="core")
