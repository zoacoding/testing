import streamlit as st
import pandas as pd

df = pd.read_csv('us.csv', sep=',', index_col=0)

st.title('미국 증시')
st.write('네이버 해외증시에서 크롤링한 데이터입니다.')

st.header('원본 데이터')
df

st.header('막대 그래프')
st.bar_chart(df['현재가'], width=500, height=500)

st.header('영역 그래프')
st.area_chart(df['현재가'], width=500, height=350)
