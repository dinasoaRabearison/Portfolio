from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from portfolio.forms import My_User
from datetime import date

# Create your views here.
def presentation(request):
    presentation_template = loader.get_template('portfolio/presentation.html')
    return HttpResponse(presentation_template.render({},request))

def experience(request):
    experience_template = loader.get_template('portfolio/experience.html')
    return HttpResponse(experience_template.render({},request))

def competence(request):
    competence_template = loader.get_template('portfolio/competence.html')
    return HttpResponse(competence_template.render({},request))

def loisir(request):
    loisir_template = loader.get_template('portfolio/loisirs.html')
    return HttpResponse(loisir_template.render({},request))

def contact(request):
    contact_template = loader.get_template('portfolio/contact.html')
    return HttpResponse(contact_template.render({},request))

def login(request):
    login_template = loader.get_template('portfolio/login.html')
    return HttpResponse(login_template.render({},request))

def inscription(request):
    inscription_template = loader.get_template('portfolio/inscription.html')
    if request.method == 'POST':
        ajout = My_User(request.POST)
        if ajout.is_valid():
            username = ajout.cleaned_data.get('username')
            password = ajout.cleaned_data.get('password')
            nom = ajout.cleaned_data.get('nom')
            poste = ajout.cleaned_data.get('poste')
            date_inscription = date.today()
            My_User.objects.create(username=username, password=password, nom=nom, poste=poste,date_inscription=date_inscription)
            
        ajout = My_User()
    else:
        ajout = My_User()
    return HttpResponse(inscription_template.render({'form':ajout}, request))