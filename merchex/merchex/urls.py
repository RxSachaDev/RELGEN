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
from django.urls import path
from sourates import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('christianisme/', views.christ_list, name='christianisme'),
    path('accueil/',views.about, name = 'accueil'),
    path('islam/',views.sourates, name ='islam'),
    path('contactez-nous/',views.contact, name = 'contact'),
    path('merci-de-votre-message/',views.emailsent, name = 'email-sent'),
    path('judaisme/',views.juda, name = 'judaisme'),
    path('decouverte/',views.decouverte, name = 'decouverte'),
    path('conditions-generales/',views.conditions, name = 'conditions'),
    path('mentions-legales/',views.mentions, name = 'mentions'),
    path('donnees-personnelles/',views.donnees, name = 'donnees'),
    path('gestions-des-cookies/',views.cookies, name = 'cookies')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
