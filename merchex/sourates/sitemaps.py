from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    def items(self):
        return['christianisme','accueil','islam','islam_arabe','email-sent','judaisme','judaisme_hebreu','decouverte','conditions','mentions','donnees','contact']
    
    def location(self,item):
        return reverse(item)