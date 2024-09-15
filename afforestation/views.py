from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
import io
import csv


@login_required(login_url='login')
def Afforestation(request):
    return render(request,'dashboard/Afforestation.html')

@login_required(login_url='login')
def project_establish(request):
    if request.method == 'POST':
        api_url = request.POST.get('api')
        
        if api_url:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                Planted_trees.objects.filter(user=request.user).delete()
                try:
                    for item in data:
                        Planted_trees.objects.create(
                                user=request.user,
                                Project_Name=item['Project_Name'],
                                Location=item['Location'],
                                Date_of_Plantation=item['Date_of_Plantation'],
                                Species_Planted=item['Species_Planted'],
                                Area_Planted=item['Area_Planted'],
                                Number_of_Trees_Planted=item['Number_of_Trees_Planted'],
                                Planting_Density=item['Planting_Density'],
                                Action=item['Action']
                            )
                
                    return render(request, 'dashboard/projectestablishment.html', {'data': data})
            
                except:
                    return render(request, 'dashboard/projectestablishment.html', {'error': 'please check API keys'})
            else:
                return render(request, 'dashboard/projectestablishment.html', {'error': 'Failed to fetch data from API'})
        
        if 'csv_file' in request.FILES:
            csv_f = request.FILES['csv_file']
            if not csv_f.name.endswith('.csv'):
                return render(request, 'dashboard/projectestablishment.html', {'errorcsv': 'This is not a csv file.'})
            
            Planted_trees.objects.filter(user=request.user).delete()
            data_set = csv_f.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                Planted_trees.objects.create(
                    user=request.user,
                    Project_Name=column[0],
                    Location=column[1],
                    Date_of_Plantation=column[2],
                    Species_Planted=column[3],
                    Area_Planted=column[4],
                    Number_of_Trees_Planted=column[5],
                    Planting_Density=column[6],
                    Action=column[7]
                )
            return redirect('projectestablish')

    if Planted_trees:
        user_data = Planted_trees.objects.filter(user=request.user)
    return render(request, 'dashboard/projectestablishment.html',{'data':user_data})

@login_required(login_url='login')
def deldata(request,pk):
    try:
        data=Planted_trees.objects.get(pk=pk)
        data.delete()
        return redirect('datatable')
    except:
        return HttpResponse("Login Again")
    
@login_required(login_url='login')
def monitor_survival(request):
    if request.method == 'POST':
        api_url = request.POST.get('api')
        
        if api_url:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                Trees_Species.objects.filter(user=request.user).delete()
                try:
                    for item in data:
                        Trees_Species.objects.create(
                                user=request.user,
                                Species_Planted=item['Species_Planted'],
                                Growth_Rate_Height=item['Growth_Rate_Height'],
                                Growth_Rate_Diameter=item['Growth_Rate_Diameter'],
                                Survival_Rate=item['Survival_Rate'],
                                Above_Ground_Biomass=item['Above_Ground_Biomass'],
                                Below_Ground_Biomass=item['Below_Ground_Biomass'],
                                Action=item['Action']
                            )
                
                    return render(request, 'dashboard/monitor_survival.html', {'data': data})
            
                except:
                    return render(request, 'dashboard/monitor_survival.html', {'error': 'please check API keys'})
            else:
                return render(request, 'dashboard/monitor_survival.html', {'error': 'Failed to fetch data from API'})
        
        if 'csv_file' in request.FILES:
            csv_f = request.FILES['csv_file']
            if not csv_f.name.endswith('.csv'):
                return render(request, 'dashboard/monitor_survival.html', {'errorcsv': 'This is not a csv file.'})
            
            Trees_Species.objects.filter(user=request.user).delete()
            data_set = csv_f.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                Trees_Species.objects.create(
                    user=request.user,
                    Species_Planted=column[0],
                    Growth_Rate_Height=column[1],
                    Growth_Rate_Diameter=column[2],
                    Survival_Rate=column[3],
                    Above_Ground_Biomass=column[4],
                    Below_Ground_Biomass=column[5],
                    Action=column[6]
                )
            return redirect('projectestablish')

    if Trees_Species:
        user_data = Trees_Species.objects.filter(user=request.user)
    return render(request, 'dashboard/monitor_survival.html',{'data':user_data})