import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactivew Widgets')

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('20230706イラスト.png')
#     st.image(img, caption='Yamatokun Family', use_column_width=True)