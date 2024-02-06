from django.urls import path
from .views import Home, PlanetList, PlanetDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('planets/<int:id>/', PlanetDetail.as_view(), name='planet-detail'),
]
