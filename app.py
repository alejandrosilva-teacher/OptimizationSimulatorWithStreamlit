import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("📈 Quadratic Optimization Simulator")

option = st.sidebar.selectbox(
    "Choose Simulation",
    ["Rectangle in a Circle", "Rectangular Pens"]
)

# ===================================
# SIMULACIÓN 1
# ===================================

if option == "Rectangle in a Circle":

    R = 5

    x = st.slider("x", 0.1, 4.9, 2.0)

    y = np.sqrt(R**2 - x**2)
    A = 4*x*y

    st.write(f"Area = {A:.2f}")

    fig, ax = plt.subplots()

    theta = np.linspace(0,2*np.pi,400)
    ax.plot(R*np.cos(theta), R*np.sin(theta))

    rect_x = [-x,x,x,-x,-x]
    rect_y = [-y,-y,y,y,-y]

    ax.plot(rect_x,rect_y)
    ax.set_aspect('equal')

    st.pyplot(fig)
    plt.close(fig)

# ===================================
# SIMULACIÓN 2
# ===================================

else:

    x = st.slider("Width x",1.0,140.0,50.0)

    y = (300 - 2*x)/3
    A = x*y

    st.write(f"Area = {A:.2f}")

    fig, ax = plt.subplots()

    rect_x=[0,x,x,0,0]
    rect_y=[0,0,y,y,0]

    ax.plot(rect_x,rect_y)
    ax.plot([0,x],[y/2,y/2])

    ax.set_aspect('equal')

    st.pyplot(fig)
    plt.close(fig)
