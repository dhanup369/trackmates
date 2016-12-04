
from django.shortcuts import render, get_object_or_404

#from trackapp.models import Blog

# this function for home page
def home(request):
    return render(request,'trackapp/home.html',{})
