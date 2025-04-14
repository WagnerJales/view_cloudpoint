
import streamlit as st
import pandas as pd
import pyvista as pv
from streamlit_vtkjs import stpyvista

st.set_page_config(layout="wide")
st.title("Visualização de Nuvem de Pontos (.xyz)")

uploaded_file = st.file_uploader("Selecione um arquivo .xyz", type=["xyz"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, sep=' ', header=None, names=['X', 'Y', 'Z'])

    st.write("Visualizando", len(df), "pontos")

    # Cria o objeto de nuvem de pontos para PyVista
    point_cloud = pv.PolyData(df[['X', 'Y', 'Z']].values)

    # Plota com PyVista + Streamlit
    plotter = pv.Plotter(off_screen=True)
    plotter.add_points(point_cloud, render_points_as_spheres=True, point_size=5.0)
    plotter.set_background("white")
    plotter.view_isometric()
    
    stpyvista(plotter, key="nuvem_pontos")

else:
    st.info("Por favor, envie um arquivo .xyz contendo coordenadas X Y Z separadas por espaço.")
