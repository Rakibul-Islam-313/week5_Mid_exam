from typing import Any
from django.shortcuts import render,redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.

def registration(request):
    if request.method == 'POST':
        register_form = RegistrationForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account registration Successful' )
            return redirect('profile_page')
    else:
        register_form = RegistrationForm()
    return render(request,'register.html', {'form':register_form})

#class based views
class UserLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('profile_page')
    
    def form_valid(self, form):
        # if not self.request.user.is_authenticated:
        messages.success(self.request,'logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'log in information invalid')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    

class UserLogoutView(LogoutView):
    success_url = reverse_lazy('home_page')
    def get_success_url(self):
        return self.success_url

@login_required
def User_profile(request):
    user = request.user
    return render(request,'user_profile.html', {'user': user})
    
@login_required
def edit_profile(request):
    if request.method == "POST":
        profile_form = forms.ChangeUserData(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('profile_page')
    else:
        profile_form = forms.ChangeUserData(instance = request.user)
    return render(request,'edit.html', {'form' : profile_form })