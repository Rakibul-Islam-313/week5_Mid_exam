from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView,View
from .import models 
from .import forms
# Create your views here.

# def add_category(request):
#     if request.method == "POST":
#         category_form = forms.CategoryForm(request.POST)
#         if category_form.is_valid():
#             category_form.save()
#             return redirect('add_category')
#     else:
#         category_form = forms.CategoryForm()
#     return render(request,'add_category.html', {'form' : category_form})

class categoryView(View):
    model = models.Brand
    form_class = forms.BrandForm
    template_name = 'home.html'
    success_url = reverse_lazy('category_wise_car')
    
    def form_valid(self, form):
        return super().form_valid(form)
    