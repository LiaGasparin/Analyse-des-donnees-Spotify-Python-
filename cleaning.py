""" BIENVENUE DANS NOTRE MODULE 'CHARGEMENT & NETTOYAGE DE DONNEES' :) """

#Chemin relatif 

import os 
# On se place dans la partie 2 et on récupere le chemin du répertoire courant
current_path = os.getcwd()
#On remonte d'un niveau dans les dossiers
path = os.path.abspath(os.path.join(current_path, '..'))
#On joint le chemin obtenu avec le dossier 'data'
path_data = os.path.join(path, 'data')
os.chdir(path_data)


import pandas as pd

'DataFrame ARTIST'

df_art=pd.read_csv("artists.csv",encoding="utf-8")
df_art = df_art.rename(columns = {'name':'artists'}) #renomme libellé de la colonne
df_art['artists'] = df_art['artists'].str.lower()

'DataFrame TRACK'

df_track=pd.read_csv("tracks.csv",encoding="utf-8")
df_track['artists'] = df_track['artists'].replace({'\[\'': '', '\'\]': ''}, regex=True)
#supprimer les crochets et apostrophes entourant les noms d'artistes. Or ici [] sont
#des expressions régulières. On utilise donc le \ pour permettre l'utilisation de caractères 
#spéciaux sans invoquer leur signification particulière. (def docs.python)
df_track['artists'].str.lower()

#Modifications dates : 
        #transformer en to_datetime
df_track["release_date"] = pd.to_datetime(df_track["release_date"], format="%Y-%m-%d")
    #créer une nouvelle colonne pour les années de sorties
df_track["release_year"] = df_track["release_date"].dt.strftime('%Y')

'DataFrame TOP200'

df_top200 = pd.read_csv("spotify_top200_global.csv",encoding="utf-8")

'DataFrame SIGNLEPARARTISTE'

#groupe par artiste et calcule la somme des streams pour chaque artiste (alternative à .agg)
sommestream = df_top200.groupby("Artist")["Streams"].sum().reset_index() 

#groupe par artiste et compte le nombre de titres unique pour chaque artiste
singleparartiste = df_top200.groupby("Artist")["Title"].nunique().reset_index() 
singleparartiste.columns = ["Artist", "Nombre de single dans le top200"] 

def cleandata():
    return df_art, df_track, df_top200, singleparartiste