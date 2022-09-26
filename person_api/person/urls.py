from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from rest_framework import routers

#router will handle our routing and map to the right view with args route name and view
router = routers.DefaultRouter()
router.register('person', views.PersonView)
router.register('city', views.CityView)
router.register('career', views.CareerView)
router.register('album', views.AlbumView)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', obtain_auth_token)
]