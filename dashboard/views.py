from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate
from .models import *
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
# user = User.objects.get(username='prashant123')
# user.set_password('1234')
# user.save()

# from django.contrib.auth import get_user_model

# User = get_user_model()
# print(User.objects.all())
@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard/index.html')

@login_required(login_url='login')
def dashboard2(request):
    user_profile = User_Profile.objects.get(user=request.user)
    return render(request,'dashboard/index1.html',{'data':user_profile})

@login_required(login_url='login')
def retirement(request):
    return render(request,'dashboard/sustainogram-retirement.html')

@login_required(login_url='login')
def projects(request):
    return render(request,'dashboard/all-projects.html')

@login_required(login_url='login')
def detailing(request):
    return render(request,'dashboard/detail-page.html')

def issuence(request):
    data=Issuence.objects.all()
    return render(request,'dashboard/sustainogram-issuence.html',{"data":data})

class client_register(View):
    def post(self,request):
        # vintage=request.POST.get('val-vintage')
        quantity=request.POST.get('val-quantity')
        project=request.POST.get('val-project')
        product=request.POST.get('val-product')
        projectname=request.POST.get('val-projectname')
        company=request.POST.get('val-company')
        terms=request.POST.get('val-terms')
        if terms:
            def numbers_to_strings(argument):
                switcher = {
                    "1": "A/R",
                    "2": "Biogas - Cogeneration",
                    "3": "Biogas - Electricity",
                    "4": "Biogas - Heat",
                    "5": "Biogas - Transportation",
                    "6":"Biomass, or Liquid Biofuel - Cogeneration",
                    "7":"Biomass, or Liquid Biofuel - Electricity",
                    "8":"Biomass, or Liquid Biofuel - Heat",
                    "9":"CSA",
                    "10":"Clean Water Access",
                    "11":"Energy Efficiency - Agriculture Sector",
                    "12":"Energy Efficiency - Commercial Sector",
                    "13":"Energy Efficiency - Domestic",
                    "14":"Energy Efficiency - Industrial",
                    "15":"Energy Efficiency - Public Sector",
                    "16":"Energy Efficiency - Transport Sector",
                    "17":"Geothermal",
                    "18":"Liquid Biofuel - Transportation",
                    "19":"Other",
                    "20":"PV",
                    "21":"Small, Low - Impact Hydro",
                    "22":"Solar Thermal - Electricity",
                    "23":"Solar Thermal - Heat",
                    "24":"WASH",
                    "25":"Wind",
                }
                return switcher.get(argument)
            
            project = numbers_to_strings(project)
            profile=Issuence(Quantity=quantity,Project_Name=projectname,Project_Type=project,Product_type=product,Developed_BY=company)
            profile.save()
            return redirect("issuence")
    def get(self,request):
        return render(request,'dashboard/form-validation-jquery.html')

class register(View):
    def post(self,request):
        username=request.POST.get('username').strip().lower()
        email=request.POST.get('email').strip().lower()
        country=request.POST.get('country')
        mobile=request.POST.get('mobile')
        company=request.POST.get('company')
        password=request.POST.get('password').strip()
        repass=request.POST.get('repass').strip()
        if username and email and country and mobile and company and password and repass:
            if password != repass:
                context={'message2':'password doesn\'t match'}
                return render(request,'dashboard/page-register.html',context)
            check_user=User.objects.filter(username=username).first()
            check_email=User.objects.filter(email=email).first()
            if check_user or check_email:
                context={'message':'Username or Email already exist'}
                return render(request,'dashboard/page-register.html',context)
            else:
                user=User.objects.create_user(username,email,password)
                user.save()
                #addnig in group
                group=Group.objects.get(name="User")
                user.groups.add(group)

                profile=User_Profile(user=user,email=email,mobile=mobile,country=country,company=company)
                profile.save()
                profile= User_Profile.objects.filter(mobile=mobile).first()
                user=User.objects.get(id=profile.user.id)
                login(request,user)
                return redirect("homedashboard")
        else:
             return render(request,'dashboard/page-register.html',{'message':'All are required fields'})
    def get(self,request):
        return render(request,'dashboard/page-register.html')

class log_in(View):
    def post(self,request):
        username=request.POST.get('username').strip().lower()
        password=request.POST.get('password').strip()
        if "@" in username:
            username= User.objects.filter(email=username).first()
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("homedashboard")
        else:
            context={'message':'Incorrect username or password'}
            return render(request,'dashboard/page-login.html',context)
        
    def get(self,request):
        return render(request,'dashboard/page-login.html')

def attempt_logout(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
def profile(request):
    try:
        user_profile = User_Profile.objects.get(user=request.user)
        return render(request,'dashboard/app-profile.html',{'data':user_profile})
    except:
        return HttpResponse('<h2>This is Admin Account Please Register as a User</h2>')
    
def projectsfilter(request,project):
    items = Issuence.objects.filter(Project_Type__icontains=project)
    return render(request, 'dashboard/sustainogram-filtered.html', {'items': items})