from django.urls import path
from .views import Homeview, ChartData
from MyChart import views

urlpatterns = [
    path('', Homeview.as_view(), name='Homeview'),
    path('api/data', views.get_data, name='get_data'),
    path('api/chart/data', ChartData.as_view()),
]
