import requests
import json
import pandas as pd
import plotly.express as px
import streamlit as st

#urls
DOLAR = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.10813/dados?formato=json'

def plot(n_amostras=1000):
    content = requests.get(DOLAR)
    df=pd.DataFrame(content.json())
    df = df.tail(n_amostras)
    df.valor=df.valor.astype(float)
    fig=px.line(data_frame=df,x='data',y='valor')
    return fig

def main():
    #dolar()
    st.markdown("<h1 style='text-align: center; color: Black;'>Gráfico do Dolar</h1>", unsafe_allow_html=True)
    dolar_plot = plot()
    st.write(dolar_plot)

if __name__=='__main__':
    main()