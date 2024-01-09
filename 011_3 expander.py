import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('Streamlit 超入門')

st.write('Interactivew Widgets')

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')
    
expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')
expander3 = st.expander('問い合わせ3')
expander3.write('問い合わせ3の内容を書く')


# text = st.text_input('あなたの趣味を教えてください。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
#'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('20230706イラスト.png')
#     st.image(img, caption='Yamatokun Family', use_column_width=True)