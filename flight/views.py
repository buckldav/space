from django.shortcuts import render

# Create your views here.

def testview(request):
    return render(request, "flight/index.html")

def contentkeeperview(request):
    return render(request, "flight/ContentKeeper.html")

def winview(request):
    return render(request, "flight/Win.html")
