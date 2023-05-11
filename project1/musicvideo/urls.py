from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    
    path('music/',views.music,name="music"),
    path('video/',views.video,name="video"),
    path('',views.hello,name="hello")
]
