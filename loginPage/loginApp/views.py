from django.shortcuts import render
from django.template.context_processors import request
from loginApp.models import Login
from django.db.models.base import Model



# Create your views here.
def loginP(request):
    return render(request, 't.html')

def signIN(request):
    print("Welcome in sign in page...")
    print(request.method)
    print(request.POST["username"])
    un=request.POST["username"]
    print(request.POST["password"])
    psw=request.POST["password"]
    
    login=Login()
    login.username=un
    login.password=psw
    login.save()
    
    
    
    '''if un=='supriya':
        return render(request, "inbox.html")
    else:
        return render(request, "error.html")
    '''
