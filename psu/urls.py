from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('get_psu/<int:pk>', views.get_psu, name="get_psu"),
]
