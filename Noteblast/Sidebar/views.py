from django.shortcuts import render
from django.views.generic import ListView
from Sidebar.models import SideBar, Trash
from django.http import HttpResponse
# Create your views here.

class StartPageView(ListView):
    template_name = "base.html"
    model  = SideBar
    model = Trash
 
def HomePage(request):
    return render (request,'base.html')


