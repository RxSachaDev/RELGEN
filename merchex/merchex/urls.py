"""
URL configuration for merchex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from sourates import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('christianisme/', views.christ_list, name='christianisme'),
    path('',views.about, name = 'accueil'),
    path('islam/francais',views.sourates, name ='islam'),
    path('islam/arabe',views.sourates_arabe, name ='islam_arabe'),
    path('merci-de-votre-message/',views.emailsent, name = 'email-sent'),
    path('judaisme/francais',views.juda, name = 'judaisme'),
    path('judaisme/hebreu',views.juda_hebreu, name = 'judaisme_hebreu'),
    path('decouverte/',views.decouverte, name = 'decouverte'),
    path('conditions-generales/',views.conditions, name = 'conditions'),
    path('mentions-legales/',views.mentions, name = 'mentions'),
    path('donnees-personnelles/',views.donnees, name = 'donnees'),
    path('contactez-nous/',views.contact, name = 'contact')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'sourates.views.custom_404'

