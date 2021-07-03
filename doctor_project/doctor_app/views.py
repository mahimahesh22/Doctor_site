from django.shortcuts import render
from django.http import HttpResponse
from doctor_app.forms import Doctorsite
from doctor_app.models import Doctor


# Create your views here.
def terminate(request):
    return render(request,"doctor_app/terminate.html")

def index(request):
    #return HttpResponse("Basic One")
    mydict={"val":"press is okay"}
    return render(request,"doctor_app/index.html",context=mydict)


def patient(request):
    #return HttpResponse("Basic One")

    form=Doctorsite

    if request.method =='POST':
        form =Doctorsite(request.POST)


        try:

          if form.is_valid():

             form.save(commit=True)

             return terminate(request)

          else:
             print("Error form Invalid")
        except:
            print("Error")
    return render(request,'doctor_app/patient.html',{'forms':form})



def discharge(request):
    #return HttpResponse("Basic One")

    webpages_list = Doctor.objects.order_by('first_name')
    date_dict = {"access_records":webpages_list}
    return render(request,'doctor_app/discharge.html',date_dict)
