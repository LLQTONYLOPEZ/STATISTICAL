from django.shortcuts import render,HttpResponse


def index(request):
	return render(request,"index.html")

def Informacion(request):
	return render(request,"Informacion.html")

def perfil(request):
	return render(request,"perfil.html")

def login(request):
	return render(request,"login.html")

def recover(request):
	return render(request,"recover.html")

def prueba(request):
	return render(request,"prueba.html")	
