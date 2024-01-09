import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Display Image')

img = Image.open('20230706イラスト.png')
st.image(img, caption='Yamatokun Family', use_column_width=True)