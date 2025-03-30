import streamlit as st
import random
import math
import var_storage as var
import def_storage as Def

st.title(Def.greet_user())

with st.expander("**Quadratic formulas**"):
    st.text("test")
    st.latex(var.quadratic)

st.page_link("pages/page_1.py", label="Page 1")