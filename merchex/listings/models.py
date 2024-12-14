from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):
    #classe pour limiter les choix disponible du champ genre
    class Genre(models.TextChoices):
        HIP_HOP = 'HH', 'Hip Hop'  
        SYNTH_POP = 'SP', 'Synth Pop'  
        ALTERNATIVE_ROCK = 'AR', 'Alternative Rock'
    
    
    name = models.fields.CharField(max_length=100)
    biography = models.fields.CharField(max_length=100)
    year_formed = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    def __str__(self):  
        return self.name#premier champ de la table Liste

class Liste(models.Model):
   
    title = models.fields.CharField(max_length=100)
    description = models.fields.CharField(max_length=100)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(2021)])

    TYPE_CHOICES = [  
        ('Records', 'Disques'),  
        ('Clothing', 'Vêtements'),  
        ('Posters', 'Affiches'),  
        ('Miscellaneous', 'Divers'),  
    ] 
    type = models.fields.CharField(max_length=100)
    
     #Ajout de la clé étrangère band
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):  
        return self.title #premier champ de la table Liste
    
class Livre(models.Model):  
    nom = models.CharField(max_length=200)  
    description = models.TextField()  
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)  
    quantite = models.PositiveIntegerField()  
    image = models.ImageField(upload_to='books/images/')  
    date_creation = models.DateTimeField(auto_now_add=True)  
    date_modification = models.DateTimeField(auto_now=True)  

    def __str__(self):  
        return self.nom  


class Etudiant(models.Model):  
    nom = models.CharField(max_length=100)  
    prenom = models.CharField(max_length=100)  
    date_naissance = models.DateField()  
    lieu_naissance = models.CharField(max_length=100)  
    emprunt_date = models.DateTimeField(null=True, blank=True)  # Date d'emprunt  
    retour_date = models.DateTimeField(null=True, blank=True)  # Date de retour  
    livre = models.ForeignKey(Livre, on_delete=models.CASCADE, related_name='emprunts')  

    def __str__(self):  
        return f"{self.prenom} {self.nom}"
    
    
    
    
    
    
