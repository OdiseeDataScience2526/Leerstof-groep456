import streamlit as st
import pandas as pd
import numpy as np

st.title('Tweede Streamlit Dashboard')

# Een slider in de sidebar
num_points = st.sidebar.slider('Aantal punten', min_value=10, max_value=1000, value=100)

# Data genereren
data = pd.DataFrame({
    'x': np.arange(num_points),  # aantal punten aangepast als je de slider aanpast
    'y': np.random.randn(num_points).cumsum()
})

# Toon een lijnplot
st.line_chart(data.set_index('x'))

# Checkbox om tabel te tonen
if st.checkbox('Toon ruwe data'):
    st.write(data)

# Selectbox voor opties
optie = st.selectbox('Kies een kleur', ['Rood', 'Groen', 'Blauw'])
st.write(f'Je koos: {optie}')
