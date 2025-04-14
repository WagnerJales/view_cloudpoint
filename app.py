
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("Visualização de Nuvem de Pontos (.xyz)")

uploaded_file = st.file_uploader("Selecione um arquivo .xyz", type=["xyz"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=' ', header=None, names=['X', 'Y', 'Z'])

    st.write("Visualizando", len(df), "pontos")

    fig = px.scatter_3d(df, x='X', y='Y', z='Z',
                        opacity=0.8, height=800,
                        title='Nuvem de Pontos 3D (.xyz)',
                        size_max=1)
    fig.update_traces(marker=dict(size=2))
    st.plotly_chart(fig, use_container_width=True)

else:
    st.info("Por favor, envie um arquivo .xyz contendo coordenadas X Y Z separadas por espaço.")
