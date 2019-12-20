import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(150, 2)/[100, 100] + [24.986867, 121.576216],
    columns = ['lat', 'lon'])

st.map(map_data)
