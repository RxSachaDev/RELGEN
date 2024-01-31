import requests
from bs4 import BeautifulSoup
import sqlite3
import os  # Ajout d'import pour utiliser os.path
import time
from unidecode import unidecode

url = 'https://www.torah-box.com/torah-pdf/'
response =requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'html.parser')
    sections = soup.findAll('li')
    i = 2
    x = 1
    y=1
    db_file = 'db.sqlite3'
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    while i < 7:
        section=sections[i]
        texte_maj = section.text.split(' ')[0]
        texte = section.text.lower().split(' ')[0]
        txt = unidecode(texte)
        url = f'https://www.torah-box.com/torah-pdf/torah/{txt}/{y}.html'
        response =requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        p = soup.findAll('div', {'class':'texte_verset'})
        if soup.find('div', {'class':'texte_verset'}) != None:
            k=0
            z = 1
            while k < len(p):
                para = p[k]
                text = para.text.strip()
                print(x)
                
                id_value = x
                name_value = texte_maj
                verset_value = text
                n_chap_value = y
                n_verset_value = z

                cursor.execute("INSERT INTO sourates_juda (id, name, verset, n_chap, n_verset) VALUES (?, ?, ?, ?, ?)",
                        (id_value, name_value, verset_value, n_chap_value, n_verset_value))
                k += 1
                z += 1
                x += 1
            y =y+1
        else:
            i += 1 
            y = 1   
    conn.commit()
    conn.close()  
        
            

    



"""
sections = soup.findAll('li')
    i = 0
    x = 1
    l= 0
    y=1
    h2 = soup.findAll('h2')
    db_file = 'db.sqlite3'
    # Ouvrir la connexion à la base de données existante
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    while i < 66:
        section=sections[i]
        texte_maj = section.text
        texte = section.text.lower()
        txt = unidecode(texte)
        if i + 1 < 10:
            url = f'http://www.bible-en-ligne.net/bible,0{i + 1}O-{y},{txt}.php'
        elif i+1 < 40:
            url = f'http://www.bible-en-ligne.net/bible,{i + 1}O-{y},{txt}.php'
        else:
             url = f'http://www.bible-en-ligne.net/bible,{i + 1}N-{y},{txt}.php'
        response =requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        p = soup.findAll('p')
        if soup.find('div', {'class':'navigation'}) != None:
            k=0
            z = 1
            while k < len(p)-1:
                para = p[k]
                if z < 10 and y < 100:
                    text = para.text[4:].strip()
                elif z < 100 and y < 100:
                    text = para.text[5:].strip()
                elif y>99 and z < 100:
                    text = para.text[6:].strip()
                elif y>99 and z > 99:
                    text = para.text[7:].strip()
                else:
                    text = para.text[7:].strip()
                print(x)
                
                if i+1 < 6:
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 18 and i+1 > 5:
                    if l==0:
                        l = 1
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 23 and i+1 > 17:
                    if l==1:
                        l = 2
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 40 and i+1 > 22:
                    if l==2:
                        l = 3
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 44 and i+1 > 39:
                    if l==3:
                        l = 4
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 == 44:
                    if l==4:
                        l = 5
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 59 and i+1 > 44:
                    if l==5:
                        l = 6
                    element = h2[l]
                    title = element.text.strip()
                elif i+1 < 66 and i+1 > 58:
                    if l==6:
                        l = 7
                    element = h2[l]
                    title = element.text.strip()
                else :
                    if l==7:
                        l = 8
                    element = h2[l]
                    title = element.text.strip()

                id_value = x
                name_value = title
                section_value = texte_maj
                verset_value = text
                n_chap_value = y
                n_verset_value = z

                cursor.execute("INSERT INTO sourates_christ (id, name, section, verset, n_chap, n_verset) VALUES (?, ?, ?, ?, ?, ?)",
                        (id_value, name_value, section_value, verset_value, n_chap_value, n_verset_value))
                k = k + 1
                z += 1
                x += 1

            y= y +1
            z = 1
        else:
            y = 1
            i += 1    
    conn.commit()
    conn.close()
"""


"""
    sections = soup.findAll('li')
    liens = []
    i = 0
    for section in sections:
        if i < 66:
            a = section.find('a')
            lien = a['href']
            liens.append('http://www.bible-en-ligne.net/' + lien)
            i = i + 1
    print(liens)
"""            


"""
    sections = soup.findAll('li')
    i = 0
    while i < 66:
        titre = sections[i]
        a = titre.find('a')
        txt = a.text
        print(txt)
        i = i +1
"""


"""
    h2 = soup.findAll('h2')
    i=0
    while i<len(h2):
        element = h2[i]
        texte = element.text.strip()
        print(texte)
        i += 1
"""


"""
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
