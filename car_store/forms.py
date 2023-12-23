from django import forms 
from car_store.models import Cars,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars 
        fields = '__all__'
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','email','body']