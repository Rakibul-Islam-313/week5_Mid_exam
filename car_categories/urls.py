from django.urls import path 
from . import views 

urlpatterns = [
    path('categories/',views.categoryView.as_view())
]


 