from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'home.html')

def out_confirmation(request):
    return render(request, 'exit_ok.html')

def home(request):
    return render(request, 'home.html')

def exit_ok(request):
    return render(request, 'exit_ok.html')

def out_confirmation(request):
    return render(request, 'out_confirmation.html')

def logout_ok(request):
    return render(request, 'logout_ok.html')

def in_confirmation(request):
    return render(request, 'in_confirmation.html')

def in_ok(request):
    return render(request, 'in_ok.html')

def qr_reading(request):
    return render(request, 'qr_reading.html')