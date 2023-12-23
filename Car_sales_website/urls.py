from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home_page'),
    
    path('categories/<slug:brand_slug>/', views.home, name='category_wise_car'),

    path('users/', include('user.urls')),
    path('category/', include('car_categories.urls')),

    path('store/', include('car_store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
