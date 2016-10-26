from django.shortcuts import render
from .models import Heroe
from django.views.generic import View

class Home(View):
	def get(self,request):
		heroe=Heroe.objects.all()
		template_name='main.html'
		context={
		'heroes':heroe
		}

		return render(request,template_name,context)

class DetailView(View):
	def get(self,request,id):
		template_name="detalle.html"
		heroe=Heroe.objects.get(id=id)
		context={
		'heroe':heroe
		}

		return render(request,template_name,context)