from django.urls import path
from . import views

urlpatterns = [
    path('', views.default_view),
    path('anyNumber/<int:price>', views.calculate_tax),
    path('taxrate', views.tax_rate_view),
]
