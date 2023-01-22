from treatments import *
import streamlit as st
from streamlit_folium import st_folium
import plotly.graph_objs as go




#-----------------------------------------------------------------#

#Nom de la page
st.set_page_config(page_title="Squirrel IAE Dashboard")

#Sidebar
st.sidebar.header("Filtres")

##---Total des squirrel observés---##

total_squirrel


##---Répartition des squirrel selon leur âge---##

labels = age_squirrel.Age
values = age_squirrel.Count

fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.7)])

st.plotly_chart(fig, use_container_width=True)


##---Affciher les lieux où ont été aperçu les squirrel---##

# Create a selectbox for choosing between Male, Female or All
age_options = ["Tous"] + list(labels)
age_filter = st.selectbox("Filter by sex:", age_options)

@st.cache
def filter_data(data_squirrel, age_filter):
    if age_filter != "Tous":
        data_squirrel = data_squirrel[data_squirrel["Age"] == age_filter]
    return data_squirrel

   
# render map in Streamlit
st_folium(m, width=700, height=450)