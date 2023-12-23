from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView,DetailView
from . import models 
from . import forms  
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user
# Create your views here.

class cars_post(CreateView):
    model = models.Cars
    form_class = forms.CarForm
    template_name = 'home.html'
    success_url = reverse_lazy('car_post.html')
    def form_valid(self, form):
        return super().form_valid(form)

class CarDetailsPost(DetailView):
    model = models.Cars
    template_name = 'car_details.html'
    pk_url_kwarg = 'id'

    def post(self, *args, **kwargs):
            comment_form = forms.CommentForm(data=self.request.POST)
            post = self.get_object()
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post 
                new_comment.save()
            return self.get(self, *args, **kwargs)
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = forms.CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context 
    
# @login_required
def buy_car(request,id):
    car = get_object_or_404(models.Cars, pk=id)
    if request.method == 'POST':
        if car.quantity > 0:
            order = models.Order(user=request.user, car=car)
            order.save()
            car.quantity -= 1
            car.save()
            messages.success(request, 'You brought a car Successfully')
            return redirect('order_history_page')
        else:
            return render(request, 'out_of_stock.html', 
            {'car': car})
    return render(request,'Buy_car.html',{'car':car})

# @login_required
def view_order_history(request):
    user = get_user(request)
    orders = models.Order.objects.filter(user=user)
    return render(request, 'oder_history.html', {'orders': orders})
