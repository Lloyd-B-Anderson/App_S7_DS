import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Market Analysis')

hist_check = st.checkbox('Construir histograma') # Crear boton de hist
if hist_check: # Al hacer clic en boton (True/False)
    st.write('Creacion de un histograma para el conjunto de datos del odometro de un vehiculo')

    # Crear hist
    fig = px.histogram(car_data, x='odometer')

    # Mostrar graficos con plotly 
    st.plotly_chart(fig, use_container_width=True)

disp_check = st.checkbox('Construir grafico de dispersion')

if disp_check: # Al hacer clic crea la grafica de disp
    st.write('Creacion de un grafico de dispersion en relacion con el odometro y el precio')

    # Crear grafico
    fig = px.scatter(car_data, x = 'odometer', y = 'price',
                     labels = {'odometer': 'Odometer (Mi)',
                               'price':'Price (USD)'},
                     title = 'Scatter plot between vehicle\'s odometer and price')    
    
    # Mostrar grafico
    st.plotly_chart(fig, use_container_width=True)
