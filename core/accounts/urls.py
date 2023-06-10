from rest_framework.routers import SimpleRouter
from django.urls import path
from . import views


router = SimpleRouter(trailing_slash=False)
router.register(r'accounts', views.AccountViewSet, basename='accounts')

urlpatterns = router.urls
