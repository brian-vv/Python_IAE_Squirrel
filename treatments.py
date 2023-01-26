import pandas as pd 



#Lecture des fichers
data_squirrel = pd.read_csv('datas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

##---Total des squirrel observés---##

total_squirrel = data_squirrel.Unique_Squirrel_ID.nunique()


##---Répartition des squirrel selon leur âge---##

age_squirrel = data_squirrel.Age.value_counts().reset_index()
age_squirrel = age_squirrel.rename(columns={'index':'Age', 'Age':'Count'})
age_labels = age_squirrel['Age'].dropna().unique()
values = age_squirrel.Count


##---Afficher les apparissions des squirrel par jours dans le mois---##

# Convertire le colonne 'Date' en datetime format
data_squirrel['Date'] = pd.to_datetime(data_squirrel['Date'], format='%m%d%Y')

#Extraction du jour, du mois et de l'année
data_squirrel['month'] = data_squirrel['Date'].dt.strftime('%m')
data_squirrel['day'] = data_squirrel['Date'].dt.strftime('%d')
data_squirrel['year'] = data_squirrel['Date'].dt.strftime('%Y')

#Grouper les données par jour et compter les occurences pour avoir le nombre d'apparition
data_squirrel_grouped = data_squirrel.groupby(['day']).size()

#Création d'une ranger de jours pour 1 mois (changer la période)
date_range = pd.date_range(start='1/1/2018', end='12/31/2018', freq='D')
date_range = date_range.strftime('%d')

#Réindexer toutes les données pour inclure les jours manquant dans le fichier de données et y ajouter 0
data_squirrel_grouped = data_squirrel_grouped.reindex(date_range, fill_value=0)


##---Affciher les lieux où ont été aperçu les squirrel---##

shift_squirrel = data_squirrel['Shift'].dropna().unique()
Primary_Fur_Color_squirrel = data_squirrel['Primary_Fur_Color'].dropna().unique()
Highlight_Fur_Color_squirrel = data_squirrel['Highlight_Fur_Color'].dropna().unique()




