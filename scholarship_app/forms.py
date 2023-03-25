from django import  forms
from django.forms import ModelForm
from .models import Personal_Information,GENDER_OPTIONS,GUARDIAN_OPTIONS,Guardian_Information,School_Information,LEVEL_OPTIONS  

class Personal_Form(forms.ModelForm):
    Gender = forms.ChoiceField(choices=GENDER_OPTIONS,
    widget=forms.RadioSelect,initial='male')
    
    class Meta:
        model=Personal_Information   
        fields="__all__" 
class Guardian_Form(forms.ModelForm):
    Role = forms.ChoiceField(choices=GUARDIAN_OPTIONS,
    widget=forms.RadioSelect,initial='father')
    
    class Meta:
        model=Guardian_Information  
        fields="__all__" 
class School_Form(forms.ModelForm):
    Level = forms.ChoiceField(choices=LEVEL_OPTIONS,
    widget=forms.RadioSelect,initial='100')
    
    class Meta:
        model=School_Information   
        fields="__all__" 
