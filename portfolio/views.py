from django.shortcuts import render
from .models import Project, Languages

def home(request):
    projects = Project.objects.all()
    languages = Languages.objects.all()
    programming = Languages.objects.filter(type="prog")
    web = Languages.objects.filter(type="web")
    db = Languages.objects.filter(type = "db")
    cloud_analytics = Languages.objects.filter(type="CloudAnalytics")
    other = Languages.objects.filter(type="other")

    return render(request, 'portfolio/home.html', {'projects':projects,'prog':programming,'web':web,'db':db,'cloudAnalytics':cloud_analytics,'other':other,'lang':languages})
