from django.shortcuts import render
# Create your views here.
def music(request):
    return render(request,'music.html')

def video(request):
    return render(request,'video.html')

def hello(request):
    return render(request,'hello.html')