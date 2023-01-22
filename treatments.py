import pandas as pd 
import folium


#Lecture des fichers
data_squirrel = pd.read_csv('datas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

##---Total des squirrel observés---##

total_squirrel = data_squirrel.Unique_Squirrel_ID.nunique()


##---Répartition des squirrel selon leur âge---##

age_squirrel = data_squirrel.Age.value_counts().reset_index()
age_squirrel = age_squirrel.rename(columns={'index':'Age', 'Age':'Count'})


##---Affciher les lieux où ont été aperçu les squirrel---##
 
# Create an empty map
m = folium.Map(location=[40.78378252, -73.96885747], zoom_start=18)

# Add markers to the map
for index, row in data_squirrel.iterrows():
    folium.Marker([row['Y'], row['X']]).add_to(m)

