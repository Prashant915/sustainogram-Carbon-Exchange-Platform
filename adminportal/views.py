from django.shortcuts import render,redirect
from .forms import *
from dashboard.models import *
from django.contrib.auth import login,authenticate
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib import messages 

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            user = fm.save(commit=False)  # Save the form, but don't commit yet
            user.is_active = True
            user.is_staff = True
            user.is_superuser = True
            user.save()  # Now save the user object to the database
            # Creating the User_Profile entry after the user has been saved
            profile = User_Profile.objects.create(
                user=user,
                email=user.email,  # email from the user object
                mobile="0000000000",  # default/placeholder mobile value
                country="Not specified",  # default/placeholder country value
                company="Not specified"  # default/placeholder company value
            )
            profile.save()  # Save the profile to the database
            return redirect("userdashboard")
        else:
            return render(request, 'useradmin/userregister.html', {'form': fm})
    else:
        fm = SignUpForm()
        return render(request, 'useradmin/userregister.html', {'form': fm})



class sign_in(View):
    def post(self,request):
        username=request.POST.get('login').strip().lower()
        password=request.POST.get('password').strip()
        if "@" in username:
            username= User.objects.filter(email=username).first()
            
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("userdashboard")
        else:
            context={'message':'Incorrect username or password'}
            return render(request,'useradmin/userlogin.html',context)
    def get(self,request):
        if not request.user.is_authenticated:
            return render(request,'useradmin/userlogin.html')
        return redirect("userdashboard")
    
@login_required(login_url='userlogin')
def userprofile(request):
    fm = EditUserProfile(instance=request.user)
    
    if request.method == "POST":
        fm = EditUserProfile(request.POST, instance=request.user)
        
        if fm.is_valid():
            user = fm.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, "Profile updated successfully!")  
        else:
            messages.error(request, f"Form is invalid: {fm.errors}")

    return render(request, 'useradmin/userprofile.html', {'form': fm})
    

@login_required(login_url='userlogin')
def userdashboard(request):
    counting=User.objects.count()
    return render(request,'useradmin/userdashboard.html',{"count":counting})


@login_required(login_url='userlogin')
def user_data(request):
    if request.method == "POST":
        if request.user.is_superuser == True:
            fm= EditUserProfile(request.POST,instance=request.user)
            users = User.objects.all()
        else:
            fm= EditUserProfile(request.POST,instance=request.user)
            users = None
        if fm.is_valid():
            fm.save()
    else:
        if request.user.is_superuser == True:
            fm= EditUserProfile(instance=request.user)
            users= User.objects.all()
        else:
            fm= EditUserProfile(instance=request.user)
            users=None
    return render(request,'useradmin/allusers.html',{'form':fm,'users':users})

@login_required(login_url='userlogin')
def proissuence(request):
    data=Issuence.objects.all()
    return render(request,'useradmin/issuence.html',{"data":data})

@login_required(login_url='userlogin')
def issuencedetails(request,id):
    dta = get_object_or_404(Issuence, pk=id)
    if request.method == 'POST':
        dta.Vintage = request.POST.get('vintage', dta.Vintage)
        dta.Quantity = request.POST.get('quantity', dta.Quantity)
        dta.Project_Name = request.POST.get('projectname', dta.Project_Name)
        dta.Developed_BY = request.POST.get('developed', dta.Developed_BY)
        dta.Project_Type = request.POST.get('project', dta.Project_Type)
        dta.Product_type = request.POST.get('Producttype', dta.Product_type)
        dta.save()
        return redirect("userissuence")
    else:
        return render(request,'useradmin/issuencedetails.html',{'data':dta})


@login_required(login_url='userlogin')
def allprofile(request, id):
    user_instance = get_object_or_404(User, pk=id)
    
    if request.method == "POST":
        fm = EditUserProfile(request.POST, instance=user_instance)
        if fm.is_valid():
            fm.save()
            return redirect("allusers")
        else:
            messages.error(request, f"Form is invalid: {fm.errors}")
    else:
        fm = EditUserProfile(instance=user_instance)
        return render(request, 'useradmin/userdetails.html', {'form': fm})
    return render(request, 'useradmin/userdetails.html', {'form': fm})

def delprofile(request,id):
    user_instance = get_object_or_404(User, pk=id)
    user_instance.delete()
    return redirect("allusers")

def delissuence(request,id):
    issue= get_object_or_404(Issuence,pk=id)
    issue.delete()
    return redirect("userissuence")
