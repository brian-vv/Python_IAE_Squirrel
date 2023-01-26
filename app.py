from treatments import *
import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.graph_objs as go




#-----------------------------------------------------------------#

#Nom de la page
st.set_page_config(page_title="Squirrel IAE Dashboard", layout='wide')

#Sidebar
st.sidebar.header("Filtres")

#Body

col1, col2 = st.columns(2)
with col1: 

##---Répartition des squirrel selon leur âge---##

    fig = go.Figure(data=[go.Pie(labels=age_labels, values=values, hole=.7)])

    st.plotly_chart(fig, use_container_width=True)

with col2: 

##---Afficher les apparissions des squirrel par jours dans le mois---##

    #Création de la figure
    fig = go.Figure(data=[go.Scatter(x=data_squirrel_grouped.index, y=data_squirrel_grouped.values,mode='lines+markers')])

    #Ajout des titres
    fig.update_layout(title="Nombre d'observations par jour sur le mois d'octobre", xaxis_title="Jour", yaxis_title="Nombre d'observations")

    #Affichage sur Streamlit
    st.plotly_chart(fig, use_container_width=True,config={'displayModeBar': False, 'scrollZoom': False})


##---Affciher les lieux où ont été aperçu les squirrel selon une liste de filtre : Age, couleur de fourrure, etc..---##

#Création des options des filtres
age_options = list(age_labels)
shift_options = list(shift_squirrel)
Primary_Fur_Color_option = list(Primary_Fur_Color_squirrel)
Highlight_Fur_Color_option = list(Highlight_Fur_Color_squirrel)

#Création des filtres et disposition 
selected_ages = st.sidebar.multiselect("Age", age_options, default=age_options)
selected_shifts = st.sidebar.multiselect("Shift", shift_options, default=[])
selected_Primary_Fur_Color = st.sidebar.multiselect("Primary_Fur_Color", Primary_Fur_Color_option, default=[])
selected_Highlight_Fur_Color = st.sidebar.multiselect("Highlight_Fur_Color", Highlight_Fur_Color_option, default=[])

#Création de la map avec le choix de tous filtres et de compatge de marker qui vont être placés sur la map 
map = folium.Map(location=[40.78378252, -73.96885747], zoom_start=14)

colors = {"Adult": "blue", "Juvenile": "green", "?": "red"}

count_marker = 0 

for index, row in data_squirrel.iterrows():
        if not selected_ages or row['Age'] in selected_ages:
            if not selected_shifts or row['Shift'] in selected_shifts:
                if not selected_Primary_Fur_Color or row['Primary_Fur_Color'] in selected_Primary_Fur_Color:
                    if not selected_Highlight_Fur_Color or row['Highlight_Fur_Color'] in selected_Highlight_Fur_Color:
                        age = row['Age']
                        color = colors[age]
                        folium.Marker([row['Y'], row['X']], icon=folium.Icon(color=color)).add_to(map)
                        count_marker += 1

#Ajout de la map sur Streamlit
st.write("Il y a eu " + str(count_marker) + " de squirrel observés")

st_folium(map, width=1275, height=500)


##---Total des squirrel observés---##

total_squirrel