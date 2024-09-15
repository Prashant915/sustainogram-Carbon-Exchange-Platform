from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import requests
import io
import csv
from collections import defaultdict
import datetime

@login_required(login_url='login')
def Electricvehicle(request):
    data = evusage.objects.all()
    monthly_km = defaultdict(int)
    
    current_year = None
    for i in data:
        year = i.Sold_Date.year
        month = i.Sold_Date.strftime('%Y-%m')  
        

        if current_year is None:
            current_year = year
        elif year != current_year:
            current_year = year
            monthly_km.clear()
        
        monthly_km[month] += i.Daily_Operational_KM*30
    # Prepare data for the graph
    graph_data = sorted(monthly_km.items())  # Sort by month
    x_data = [item[0] for item in graph_data]
    y_data = [item[1] for item in graph_data]
    print(x_data)
    print(y_data)
    context = {
        'x_data': x_data,
        'y_data': y_data
    }
    return render(request,'dashboard/Electric Vehicle.html',context)

@login_required(login_url='login')
def datapoints(request):
    if request.method == 'POST':
        api_url = request.POST.get('api')
        
        if api_url:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                ApiData.objects.filter(user=request.user).delete()
                try:
                    for item in data:
                        ApiData.objects.create(
                                user=request.user,
                                Vehicle_Model_No=item['Vehicle_Model_No'],
                                Type_of_Material=item['Type_of_Material'],
                                Supplier_Name=item['Supplier_Name'],
                                Weight_of_Material=item['Weight_of_Material'],
                                Percentage_Composition=item['Percentage_Composition']
                            )
                
                    return render(request, 'dashboard/embodiescarbon.html', {'data': data})
            
                except:
                    return render(request, 'dashboard/embodiescarbon.html', {'error': 'please check API keys'})
            else:
                return render(request, 'dashboard/embodiescarbon.html', {'error': 'Failed to fetch data from API'})
        
        if 'csv_file' in request.FILES:
            csv_f = request.FILES['csv_file']
            if not csv_f.name.endswith('.csv'):
                return render(request, 'dashboard/embodiescarbon.html', {'errorcsv': 'This is not a csv file.'})
            
            ApiData.objects.filter(user=request.user).delete()
            data_set = csv_f.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                ApiData.objects.create(
                    user=request.user,
                    Vehicle_Model_No=column[0],
                    Type_of_Material=column[1],
                    Supplier_Name=column[2],
                    Weight_of_Material=column[3],
                    Percentage_Composition=column[4]
                )
            return redirect('datatable')

    if ApiData:
        user_data = ApiData.objects.filter(user=request.user)
    return render(request, 'dashboard/embodiescarbon.html',{'data':user_data})

def deldata(request,pk):
    try:
        data=ApiData.objects.get(pk=pk)
        data.delete()
        return redirect('datatable')
    except:
        return HttpResponse("Login Again")

@login_required(login_url='login')
def evusages(request):
    if request.method == 'POST':
        api_url = request.POST.get('api2')
        
        if api_url:
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                evusage.objects.filter(user=request.user).delete()
                try:
                    for item in data:
                        evusage.objects.create(
                                user=request.user,
                                Vehicle_Model_No = item['Vehicle_Model_No'],
                                Vehicle_ID = item['Vehicle_ID'],
                                Owner_Name = item['Owner_Name'],
                                Sold_Date = item['Sold_Date'],
                                Daily_Operational_KM = item['Daily_Operational_KM'],
                                Total_KM_Operation = item['Total_KM_Operation'],
                                Source_of_Power = item['Source_of_Power']
                            )
                
                    return render(request, 'dashboard/EVusage.html', {'data': data})
            
                except:
                    return render(request, 'dashboard/EVusage.html', {'error': 'please check API keys'})
            else:
                return render(request, 'dashboard/EVusage.html', {'error': 'Failed to fetch data from API'})
        
        if 'csv_file' in request.FILES:
            csv_f = request.FILES['csv_file']
            if not csv_f.name.endswith('.csv'):
                return render(request, 'dashboard/EVusage.html', {'errorcsv': 'This is not a csv file.'})
            
            evusage.objects.filter(user=request.user).delete()
            data_set = csv_f.read().decode('UTF-8')
            io_string = io.StringIO(data_set)
            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="|"):
                evusage.objects.create(
                    user=request.user,
                    Vehicle_Model_No=column[0],
                    Vehicle_ID=column[1],
                    Owner_Name=column[2],
                    Sold_Date=column[3],
                    Daily_Operational_KM=column[4],
                    Total_KM_Operation=column[5],
                    Source_of_Power=column[6]
                )
            return redirect('evusage')

    if evusage:
        user_data = evusage.objects.filter(user=request.user)
    return render(request, 'dashboard/EVusage.html',{'data':user_data})


