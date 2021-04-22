import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd

st.title('Lucas Data Science Projekt')
st.write('ich probier mal rum')
data = pd.DataFrame({'einsZeile': [1, 2, 3, 4, 5], 'zweiZeile': [34, 12, 76, 17, 10]})
st.write(data)
st.line_chart(data)
