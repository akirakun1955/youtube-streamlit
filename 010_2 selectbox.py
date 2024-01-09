import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

option = st.selectbox(
    'あなたが好きな数字を教えてください。',
    list(range(1, 11))
)

'あなたの好きな数字は、', option, 'です。'

# if st.checkbox('Show Image'):
#     img = Image.open('20230706イラスト.png')
#     st.image(img, caption='Yamatokun Family', use_column_width=True)