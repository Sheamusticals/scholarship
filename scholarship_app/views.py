from django.shortcuts import render,redirect
from .forms import Personal_Form,Guardian_Form,School_Form
from django.http import HttpResponse





# Create your views here.
def main(request):
    form =Personal_Form(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request,'main.html',{'form':form})
    
def guardian_form(request):
    form =Guardian_Form(request.POST)
    if request.method == "POST":
       
        if form.is_valid():
            form.save()
    return render(request,'guardian.html',{'form':form})   
def school(request):
    form =School_Form(request.POST)
    if request.method == "POST":
    
        if form.is_valid():
            form.save()
        return redirect(success)
         
    return render(request,'school.html',{'form':form})   

     

def success(request):
    return HttpResponse("Form submitted successfully,you will hear from us soon")