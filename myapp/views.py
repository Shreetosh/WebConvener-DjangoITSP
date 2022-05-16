from django.shortcuts import render, HttpResponse

def index(request):
    return render(request,'index.html')

def team1(request):
    return render(request,'ITSP220001.html')

def team2(request):
    return render(request,'ITSP220002.html')

def team3(request):
    return render(request,'ITSP220003.html')

def team4(request):
    return render(request,'ITSP220004.html')

def team5(request):
    return render(request,'ITSP220005.html')

def team6(request):
    return render(request,'ITSP220006.html')

def team7(request):
    return render(request,'ITSP220007.html')

def team8(request):
    return render(request,'ITSP220008.html')




