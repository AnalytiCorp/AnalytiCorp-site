from django.shortcuts import render

# Create your views here.
def index(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def analyze(request):
  return render(request, 'analyze.html')

def automation(request):
  return render(request, 'automation.html')

def security(request):
  return render(request, 'security.html')