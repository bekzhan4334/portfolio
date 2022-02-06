from django.shortcuts import render
from django.http import HttpResponse
from .models import Info

import random

def home(request):
    if request.method == "POST":
        FIO = request.POST['FIO']
        INN = request.POST['INN']
        email = request.POST['email']
        phone = request.POST['phone']
        date_of_birth = request.POST['date_of_birth']
        sex = request.POST['sex']
        nationality = request.POST['nation']
        cityzen = request.POST['cityzen']
        status = request.POST['status']
        if request.POST['orhan'] == 'on':
            orhan = True
        else:
            orhan = False
        if request.POST['invalid'] == 'on':
            invalid = True
        else:
            invalid = False
        country = request.POST.get('country')
        region = request.POST['region']
        district = request.POST.get('district')
        city = request.POST['city']
        village = request.POST.get('village')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        delo = Info(FIO=FIO, INN=INN, email=email, phone=phone, date_of_birth=date_of_birth, sex=sex, nationality=nationality,citizenship=cityzen, status=status,
                    orhan=orhan, disabled=invalid, country=country, region=region, district=district, city=city, village=village,
                    address1=address1, address2=address2)
        delo.save()
        print("The data has been saved to db")

    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')



