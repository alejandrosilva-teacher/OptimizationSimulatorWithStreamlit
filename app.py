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
    st.subheader("Mathematical Model")

    st.latex(r"x^2 + y^2 = 25")

    st.latex(r"y=\sqrt{25-x^2}")

    st.latex(r"A(x)=4x\sqrt{25-x^2}")

    st.latex(
    rf"A({x:.2f}) = 4({x:.2f})\sqrt{{25-({x:.2f})^2}} = {A:.2f}"
    )

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
    st.subheader("Mathematical Model")

    st.latex(r"2x + 3y = 300")

    st.latex(r"y=\frac{300-2x}{3}")

    st.latex(r"A(x)=x\left(\frac{300-2x}{3}\right)")

    st.latex(r"A(x)=100x-\frac{2}{3}x^2")

    st.latex(
    rf"A({x:.2f}) = {A:.2f}"
    )

    fig, ax = plt.subplots()

    rect_x=[0,x,x,0,0]
    rect_y=[0,0,y,y,0]

    ax.plot(rect_x,rect_y)
    ax.plot([0,x],[y/2,y/2])

    ax.set_aspect('equal')

    st.pyplot(fig)
    plt.close(fig)

