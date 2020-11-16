from django.shortcuts import render
from django.http import HttpResponse
from .models import Services
#from .data.feedback import Data
 

# Create your views here.
def home(request):
    
    # feedback = Data()
    # feedback.name = "testing data"
    # feedback.img = "why-us-1.jpg"

    # feedback1 = Data()
    # feedback1.name = "testing data"
    # feedback1.img = "why-us-2.jpg"

    service = Services.objects.all() 
    return render(request,'index.html',{'service': service})
#  return render(request,'index.html',{'feedback': feedback,'feedback1':feedback1})