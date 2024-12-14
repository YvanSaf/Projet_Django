from django import forms
from listings.models import Band
from listings.models import Liste
from .models import Livre, Etudiant 


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label='Nom')
    email = forms.EmailField(label='Email')
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea,
        label='Message'
    )


class BandForm(forms.ModelForm):  
    class Meta:  
        model = Band  
        #fields = '__all__'  # Inclut tous les champs du modèle 
        exclude = ('active', 'official_homepage')  # Exclut ces champs du formulaire  



class ListeForm(forms.ModelForm):  
    class Meta:  
        model = Liste 
        #fields = '__all__'  # Inclut tous les champs du modèle 
        fields = '__all__'  # Inclut tous les champs du modèle



class LivreForm(forms.ModelForm):  
    class Meta:  
        model = Livre  
        fields = '__all__'  

class EtudiantForm(forms.ModelForm):  
    class Meta:  
        model = Etudiant  
        fields = '__all__'