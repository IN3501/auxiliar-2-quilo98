from django.shortcuts import render

# Create your views here.
def ED(request):
	return render(request, 'miapp/ED.html')

def index(request):
	return render(request, 'miapp/index.html')

def logrado(request):
	return render(request, 'miapp/logrado.html')
	