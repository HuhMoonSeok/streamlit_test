import streamlit as st
import pandas as pd

view = [100,150,60]
st.write('# Title')
view
st.write('# bar chart')
st.bar_chart(view)
sview = pd.Series(view)
sview