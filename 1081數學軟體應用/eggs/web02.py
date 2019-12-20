import streamlit as st
import pandas as pd

st.title("我的沒有用的網頁")

df = pd.DataFrame({
    "A":[54, 32, 99],
    "B":[94, 87, 6502]
})

st.write(df)