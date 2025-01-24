from django.shortcuts import render
from human_resource.models import *
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def Dashboard(request):
    employees = Employee.objects.all().count
    context = {"employees":employees}
    return render(request, 'dashboard/analytics.html', context)