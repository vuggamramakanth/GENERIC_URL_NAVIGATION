from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hai(request):
    return render(request,'hai.html')

def bye(request):
    return render(request,'bye.html')