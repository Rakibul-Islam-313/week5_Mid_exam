from django.urls import path 
from . import views

urlpatterns = [
    path('cars/', views.cars_post.as_view(), name='cars_post_page'),

    path('car_detail/<int:id>', views.CarDetailsPost.as_view(), name='car_detail_page'),

    path('history/', views.view_order_history, name= 'order_history_page'),

    path('buy/<int:id>/', views.buy_car, name = 'brought_car')
]
