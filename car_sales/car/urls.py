from django.urls import path 
from . import views 
urlpatterns = [
    path('' , views.home, name='homepage'),
    path('brand/<slug:brand_slug>/', views.home, name='brand_wise_serial'),
    path('details/<int:id>/', views.details.as_view(), name='details'),
    path('buy/<int:id>/', views.buycar.as_view(), name='buy_car'),
    
]
