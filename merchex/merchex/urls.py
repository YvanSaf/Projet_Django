
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from listings import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band_list'),
    path('about/', views.about),
    path('contact/', views.contact),
    path('liste/', views.liste_list, name='liste_list'),
    path('liste/<int:id>/', views.liste_detail, name='liste_detail'),
    path('liste/add/', views.liste_create, name='liste_create'),
    path('liste/<int:id>/change/', views.liste_update, name='liste_update'), 
    path('liste/<int:id>/delete/', views.liste_delete, name='liste_delete'), 
    path('bands/<int:id>/', views.band_detail, name='band_detail'),  # Chemin pour la vue détaillée  
    path('bands/<int:id>/change/', views.band_update, name='band_update'),
    path('bands/<int:id>/delete/', views.band_delete, name='band_delete'),
    path('bands/add/', views.band_create, name='band_create'), 
    path('livre/', views.livre_list, name='livre_list'),
    path('livre/add/', views.livre_create, name='livre_create'),
    path('livre/<int:id>/change/', views.livre_update, name='livre_update'), 
    path('livre/<int:id>/delete/', views.livre_delete, name='livre_delete'), 
    path('student/', views.student_list, name='student_list'),
    path('student/add/', views.student_create, name='student_create'),
    path('student/<int:id>/change/', views.student_update, name='student_update'), 
    path('student/<int:id>/delete/', views.student_delete, name='student_delete')
    
] +static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
