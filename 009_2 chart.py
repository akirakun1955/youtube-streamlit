import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit 超入門')

st.write('DataFrame')

df = pd.DataFrame(
    np.random.rand(20, 3) ,
    columns = ['a', 'b', 'c']
)


#静的
# st.table(df.style.highlight_max(axis=0))

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)