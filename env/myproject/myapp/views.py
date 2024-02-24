from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')
def munnar(request):
    return render(request,'munnar.html')
def alleppy(request):
    return render(request,'alleppy.html')
def thirdP(request):
    return render(request,'thirdP.html')
def forthP(request):
    return render(request,'forthP.html')
def destinations(request):
    return render(request,'destinations.html')
def contact(request):
    return render(request,'contact.html')
def review(request):
    return render(request,'review.html')