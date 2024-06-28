import streamlit as st
import numpy as np
import pandas as pd

st.title('streamlit')

st.write('dataFlame')

df = pd.dataFlame({
    '1列目':[1,2,3,4],
    '2列目':[10,20,30,40]
})


st.dataFlame(df.style.highlight_max(axis=100))
