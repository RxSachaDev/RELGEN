import requests
from bs4 import BeautifulSoup
import sqlite3
import os  # Ajout d'import pour utiliser os.path
import time

url = 'https://www.le-coran.com'
lignes = []
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

if response.ok:
    
    elements = soup.findAll('span', {'class': 'transcription'})
    i = 1
    y = 1
    k = 1
    
    while i < 115:
        sourate = elements[i-1]
        if i < 99 :
            sourates = sourate.text[3:].strip()
        else :
            sourates = sourate.text[5:].strip() 
        url = 'https://www.le-coran.com/coran-francais-sourate-'+str(i)+'-0.html'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Vérifier si la base de données existe
        db_file = 'db.sqlite3'
        # Ouvrir la connexion à la base de données existante
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        k=1
        while soup.find('p', {'class': 'verset_pos_' + str(k)}) != None:
            ps = soup.find('p', {'class': 'verset_pos_' + str(k)})
            if k < 10:
                verse_text = ps.text[2:].strip()
            elif k < 100 and k >= 10:
                verse_text = ps.text[3:].strip()
            else:
                verse_text = ps.text[4:].strip()
            # Données à insérer
            id_value = y
            name_value = sourates
            verset_value = verse_text
            n_verset_value = k

                # Utilisation de paramètres de requête pour éviter les problèmes d'apostrophes
            cursor.execute("INSERT INTO sourates_sourate (id, name, verset, n_verset) VALUES (?, ?, ?, ?)",
                        (id_value, name_value, verset_value, n_verset_value))

            y += 1
            print(k)
            k += 1
        i+=1
        # Validez la transaction et fermez la connexion après la boucle
        conn.commit()
        conn.close()





"""
    while i < 114:
        sourate = elements[i]
        if i < 99 :
            sourates = sourate.text[3:].strip()
        else :
            sourates = sourate.text[5:].strip() 
        
        i += 1
"""



"""
    # Vérifier si la base de données existe
    db_file = 'db.sqlite3'
    if not os.path.exists(db_file):
        print("La base de données n'existe pas à l'emplacement spécifié.")
    else:
        # Ouvrir la connexion à la base de données existante
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()

        i = 1
        while i < 177:
            ps = soup.find('p', {'class': 'verset_pos_' + str(i)})
            verse_text = ps.text[2:].strip()

            # Données à insérer
            id_value = i + 669
            name_value = 'AL-FATIHA'
            verset_value = verse_text
            n_verset_value = i

            # Utilisation de paramètres de requête pour éviter les problèmes d'apostrophes
            cursor.execute("INSERT INTO sourates_sourate (id, name, verset, n_verset) VALUES (?, ?, ?, ?)",
                           (id_value, name_value, verset_value, n_verset_value))

            i += 1

        # Validez la transaction et fermez la connexion après la boucle
        conn.commit()
        conn.close()
"""