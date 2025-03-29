import streamlit as st
import random

greetings = ["Hi there, what :rainbow[Math equation] do need?"
             ,"We got some :rainbow[Math equation] at the mathinator"
             ,":rainbow[Quadratic, linear, area, volume,] :rainbow[Math equations]? We got them all"]

st.subheader(random.choice(greetings))

st.subheader("")

st.latex(r'''
x = \frac{-(b)^2 \pm \sqrt{(b^2 -4ac) }} {2a}
''')

st.latex('''
a^2 + b^2 = c^2
''')

st.latex('''
\pi r^2 =a
''')