# 유용함 Streamlit
import streamlit as st

numbers = [10, 20, 30, 40, 50]

st.write('# Numbers')
st.write('## Raw Data')
numbers

st.write('## Graph')
st.line_chart(numbers)
