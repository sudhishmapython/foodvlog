from django.urls import path
from . import views

urlpatterns = [
   path('',views.view,name='view'),
   path('<slug:c_slug>/',views.view,name='prod_cat'),
   path('<slug:c_slug>/<slug:pro_slug>',views.prodDetails,name='details'),
   path('search',views.searching,name='search')
]