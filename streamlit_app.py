import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({
    'x': range(10),
    'y': [i**2 for i in range(10)]
})

st.write(data)

plt.plot(data['x'], data['y'])
st.pyplot(plt)
