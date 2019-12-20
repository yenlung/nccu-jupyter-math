import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

coffee = st.slider("咖啡粉量", 10.0,
                  45.0, 
                  20.0,
                  0.5)
water = 15*coffee

st.write(f"咖啡粉 {coffee} 克, 請使用 {water} 克的水")
