from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'pages/Home.html')


def zzana(request):
    return render(request,'pages/zzana-campus.html')

def ndejje(request):
    return render(request,'pages/ndejje-campus.html')