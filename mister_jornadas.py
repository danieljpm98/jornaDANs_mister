# Import python packages
import streamlit as st
import requests
import json

# Creo el diccionario con las abreviaciones para las URLs
equipos = {
    'Real Betis Balompié': 'betis',
    'CD Leganés': 'leganes',
    'RCD Mallorca': 'mallorca',
    'Villarreal CF': 'villarreal',
    'RCD Espanyol de Barcelona': 'espanyol',
    'Deportivo Alavés': 'alaves',
    'Sevilla FC': 'sevilla',
    'Getafe CF': 'getafe',
    'Real Sociedad de Fútbol': 'real-sociedad',
    'Real Madrid CF': 'real-madrid',
    'RC Celta de Vigo': 'celta',
    'Real Valladolid CF': 'real-valladolid',
    'Girona FC': 'girona',
    'FC Barcelona': 'barcelona',
    'UD Las Palmas': 'las-palmas',
    'Athletic Club': 'athletic',
    'Club Atlético de Madrid': 'atletico',
    'Valencia CF': 'valencia',
    'Rayo Vallecano de Madrid': 'rayo-vallecano',
    'CA Osasuna': 'osasuna',
}

# Write directly to the app
st.title("JornaDANs Mister :soccer:")
st.write("""Las alineaciones probables de La Liga a tu alcance! :first_place_medal:""")

numero_jornada = st.text_input('Número de jornada:')

if numero_jornada:
    
    # Access the API token from Streamlit secrets
    api_token = st.secrets["api"]["token"]
    
    partidos_jornada = 'https://api.football-data.org/v4/competitions/PD/matches?matchday=' + numero_jornada
    headers = {'X-Auth-Token': api_token}

    response = requests.get(partidos_jornada, headers=headers)

    if response.status_code == 200:
        # Parse the JSON data
        data = response.json()
        
        print(f"Jornada {data['filters']['matchday']} de La Liga:")

        for match in data['matches']:
            
            local = match['homeTeam']['name']
            visitante = match['awayTeam']['name']
            print(f"{local} - {visitante}")
            url = 'https://www.jornadaperfecta.com/blog/alineaciones-' + equipos[local] + '-' + equipos[visitante] + '-jornada-' + numero_jornada + '-24-25/'
            st.link_button(f'{local} - {visitante} Jornada {numero_jornada}', url)
            st.page_link(url, label=f'{local} - {visitante}')
    else:
        # Handle errors
        print(f'Failed to retrieve data: {response.status_code}')
