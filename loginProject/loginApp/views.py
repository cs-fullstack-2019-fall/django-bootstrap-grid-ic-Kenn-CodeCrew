from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Wrong URL")

def login(request):
    nameArray = ["Kenn", "Kevin", "Erin", "Thomas"]
    return render(request,'loginApp/index.html', {"names": nameArray})


def inclass(request):
    return render(request, 'loginApp/inclass.html')