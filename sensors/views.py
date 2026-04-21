from django.shortcuts import render


# Create your views here.
def sensors(request):
    return render(request, "sensors/index.html")
