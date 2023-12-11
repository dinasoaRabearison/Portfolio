from django import forms

class My_User(forms.Form):
    username= forms.CharField(max_length = 150,error_messages={"required":'Champs obligatoire'})
    password= forms.PasswordInput()
    nom = forms.CharField(max_length=60,error_messages={"required":'Champs obligatoire'})
    poste = forms.CharField(max_length=150,error_messages={"required":'Champs obligatoire'})
    observation = forms.CharField(max_length=200,error_messages={"required":'Champs obligatoire'})
    date_inscription = forms.DateField()