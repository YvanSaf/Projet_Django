from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from listings.models import Band
from listings.models import Liste
from .models import Livre, Etudiant 
from .forms import EtudiantForm  
from .forms import LivreForm
from django.core.mail import send_mail
from listings.forms import ContactUsForm 
from django.shortcuts import redirect 
from listings.forms import BandForm 
from listings.forms import ListeForm 


def band_list(request):
    bands=Band.objects.all()
    return render(request, 'listings/band_list.html', {'bands': bands})  # Envoi des données au gabarit 

# listings/views.py  
def band_detail(request, id):  
    band = Band.objects.get(id=id)  # Récupère l'objet Band avec l'id spécifié  
    return render(request, 'listings/band_detail.html', {'band': band}) 

def liste_list(request):  
    liste = Liste.objects.all()  # Récupération de toutes les annonces  
    return render(request, 'listings/liste_list.html', {'liste': liste})  # Rendu avec le gabarit

def liste_detail(request, id):  
    liste = Liste.objects.get(id=id)  # Récupération de toutes les annonces  
    return render(request, 'listings/liste_detail.html', {'liste': liste})  # Rendu avec le gabarit  

def about(request):  
    return render(request, 'listings/about.html')  # Rendu de la page 'about'

def contact(request):  
    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
            subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=['admin@merchex.xyz'],
        )
            return redirect('email-sent')  # ajoutez cette instruction de retour
    # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
    # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

        else: 
        # ceci doit être une requête GET, donc créer un formulaire vide
         form = ContactUsForm()  # Instanciation du formulaire  
        return render(request, 'listings/contact.html', {'form': form})  # Passage du formulaire au modèle
    

def band_create(request):  
     if request.method == 'POST':  
        form = BandForm(request.POST)  
        if form.is_valid():  
            band = form.save()  # Sauvegarde le nouvel objet Band  
            return redirect('band_detail', band.id)  # Redirection vers la page de détail du groupe  
     else:  
        form = BandForm()  # Formulaire vide pour une requête GET  

     return render(request, 'listings/band_create.html', {'form': form})



def liste_create(request):  
    if request.method == 'POST':  
        form = ListeForm(request.POST)  
        if form.is_valid():  
            liste = form.save()  # Sauvegarde le nouvel objet Liste  
            return redirect('liste_detail', liste.id)  # Redirection vers la page de détail de la liste  
    else:  
        form = ListeForm()  # Formulaire vide pour une requête GET  

    return render(request, 'listings/liste_create.html', {'form': form})

def band_update(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band_detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                'listings/band_update.html',
                {'form': form})

def liste_update(request, id):
    liste = Liste.objects.get(id=id)

    if request.method == 'POST':
        form = ListeForm(request.POST, instance=liste)
        if form.is_valid():
            # mettre à jour l'annonce existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('liste_detail', liste.id)
    else:
        form = BandForm(instance=liste)

    return render(request,
                'listings/liste_update.html',
                {'form': form})


def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return redirect('band_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/band_delete.html',
                    {'band': band})


def liste_delete(request, id):
    liste = Liste.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        liste.delete()
        # rediriger vers la liste des groupes
        return redirect('band_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/liste_delete.html',
                    {'liste': liste})






def livre_list(request):  
    livre = Livre.objects.all()  # Récupération de toutes les annonces  
    return render(request, 'listings/livre_list.html', {'livre': livre})  # Rendu avec le gabarit



def livre_create(request):  
    if request.method == 'POST':  
        form = LivreForm(request.POST)  
        if form.is_valid():  
            livre = form.save()  # Sauvegarde le nouvel objet Liste  
            return redirect('livre_list')  # Redirection vers la page de liste des livres
    else:  
        form = LivreForm()  # Formulaire vide pour une requête GET  

    return render(request, 'listings/livre_create.html', {'form': form})

def livre_update(request, id):
    livre = Livre.objects.get(id=id)

    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()  # Sauvegarde les changements
            return redirect('livre_list')  # Redirige vers la liste des livres
    else:
        form = LivreForm(instance=livre)

    return render(request, 'listings/livre_update.html', {'form': form})

def livre_delete(request, id):
    livre = Livre.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        livre.delete()  # Supprime le livre
        return redirect('livre_list')  # Redirige vers la liste des livres

    return render(request, 'listings/livre_delete.html', {'livre': livre})



def student_list(request):  
    student = Etudiant.objects.all()  # Récupération de toutes les annonces  
    return render(request, 'listings/student_list.html', {'student': student})  # Rendu avec le gabarit



def student_create(request):  
    if request.method == 'POST':  
        form = EtudiantForm(request.POST)  
        if form.is_valid():  
            student = form.save()  # Sauvegarde le nouvel objet Liste  
            return redirect('student_list', student.id)  # Redirection vers la page de détail de la liste  
    else:  
        form = EtudiantForm()  # Formulaire vide pour une requête GET  

    return render(request, 'listings/student_create.html', {'form': form})

def student_update(request, id):
    student = Etudiant.objects.get(id=id)

    if request.method == 'POST':
        form = EtudiantForm(request.POST, instance=student)
        if form.is_valid():
            # mettre à jour l'annonce existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('student_list', student.id)
    else:
        form = EtudiantForm(instance=student)

    return render(request,
                'listings/student_update.html',
                {'form': form})

def student_delete(request, id):
    student = Etudiant.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
        # supprimer le groupe de la base de données
        student.delete()
        # rediriger vers la liste des groupes
        return redirect('student_list')

    # pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                    'listings/student_delete.html',
                    {'student': student})