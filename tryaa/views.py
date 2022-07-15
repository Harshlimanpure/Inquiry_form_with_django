from django.shortcuts import render , redirect
from .forms import Form
from .models import MForm
# Create your views here.
def home(request):
    if request.method == "POST":
        fm = Form(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            fnm=fm.cleaned_data['father_Name']
            mnm=fm.cleaned_data['mother_Name']
            cont=fm.cleaned_data['contact']
            adr=fm.cleaned_data['address']
            em=fm.cleaned_data['email']
            pwd=fm.cleaned_data['password']
            user = MForm(name=nm,father_name=fnm,mother_name=mnm,contact=cont,address=adr,email=em,password=pwd)
            user.save()
            
            return redirect('/') 
    else:
        fm = Form()
        return render(request, 'home.html',{'form':fm})
    return render(request, 'home.html',{'form':fm})
