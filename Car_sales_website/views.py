from django.shortcuts import render
from car_store.models import Cars
from car_categories.models import Brand

def home(request, brand_slug = None):
    data = Cars.objects.all()
    Cars_category = Brand.objects.all()
    # print(data, Cars_category)
    if brand_slug is not None:
        brand = Brand.objects.get(slug = brand_slug)
        data = Cars.objects.filter(brand = brand)
    return render(request,'home.html',{'data': data, 'Cars_category': Cars_category})
