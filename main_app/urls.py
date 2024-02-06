from django.urls import path
from .views import Home, PlanetList, PlanetDetail, MoonListCreate, MoonDetail


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('planets/', PlanetList.as_view(), name='planet-list'),
    path('planets/<int:id>/', PlanetDetail.as_view(), name='planet-detail'),
    path('planets/<int:planet_id>/moons/', MoonListCreate.as_view(), name='moon-list-create'),
    path('planets/<int:planet_id>/moons/<int:id>/', MoonDetail.as_view(), name='moon-detail'),
]
