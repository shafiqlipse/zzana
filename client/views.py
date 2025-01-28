from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'pages/Home.html')


def zzana(request):
    return render(request,'pages/zzana-campus.html')

def contact(request):
    return render(request,'pages/contact.html')

def about(request):
    return render(request,'pages/About.html')