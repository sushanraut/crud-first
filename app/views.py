from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    form=StudentForm()
    context={
        'form':form
    }

    return render(request,'home.html',context)

def index(request):
    print("hello index")
    return render(request,'index.html')
