from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.
def homepage(request):
    return render(request,'website/index.html')

class contentview(View):
    template_name=''
    def get(self,request):
        return render(request,self.template_name)
    
def resources(request):
    data=resource.objects.all()
    return render(request,'website/resource.html',{'data':data})

def summery(request,resourceid):
    data=resource.objects.get(pk=resourceid)
    return render(request,'website/summery.html',{'data':data})