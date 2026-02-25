import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("Quadratic Optimization Simulator")

problem = st.sidebar.selectbox(
    "Choose problem",
    ["Rectangle inside a circle",
     "Rectangle with internal fence (5 sides)"]
)

# ======================================================
# PROBLEMA 1 — RECTÁNGULO EN CÍRCULO
# ======================================================

if problem == "Rectangle inside a circle":

    st.header("Rectangle Inscribed in a Circle")

    R = st.sidebar.number_input(
        "Circle radius",
        min_value=1.0,
        value=5.0
    )

    x_vals = np.linspace(0.01, R, 400)
    area = 4*x_vals*np.sqrt(R**2-x_vals**2)

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(6,4))
        ax1.plot(x_vals, area)
        ax1.set_xlabel("x")
        ax1.set_ylabel("Area")
        ax1.set_title("Area Function")

        st.pyplot(fig1)
        st.latex(r"A(x)=4x\sqrt{R^2-x^2}")

    x = st.slider("Half width x",0.1,float(R-0.1),float(R/2),0.05)

    if st.button("Simulate"):

        with col2:

            y=np.sqrt(R**2-x**2)

            fig2,ax2=plt.subplots(figsize=(6,4))

            theta=np.linspace(0,2*np.pi,400)
            ax2.plot(R*np.cos(theta),R*np.sin(theta))

            rect_x=[-x,x,x,-x,-x]
            rect_y=[-y,-y,y,y,-y]

            ax2.plot(rect_x,rect_y)

            ax2.set_aspect('equal')
            ax2.set_xlim(-R*1.2,R*1.2)
            ax2.set_ylim(-R*1.2,R*1.2)

            st.pyplot(fig2)
            st.success(f"Area = {4*x*y:.2f}")

# ======================================================
# PROBLEMA 2 — CERCA CON DIVISIÓN INTERNA
# ======================================================

if problem == "Rectangle with internal fence (5 sides)":

    st.header("Maximum Area with Internal Fence")

    L = st.sidebar.number_input(
        "Total fence length",
        min_value=10.0,
        value=60.0
    )

    # MODELO CORRECTO
    x_vals=np.linspace(0.1,L/2,400)
    y_vals=(L-2*x_vals)/3
    area=x_vals*y_vals

    col1,col2=st.columns(2)

    # PARÁBOLA
    with col1:

        fig1,ax1=plt.subplots(figsize=(6,4))
        ax1.plot(x_vals,area)

        ax1.set_xlabel("Width x")
        ax1.set_ylabel("Area")
        ax1.set_title("Area Function")

        st.pyplot(fig1)

        st.latex(r"A(x)=\frac{x(L-2x)}{3}")

    x=st.slider(
        "Width x",
        0.5,
        float(L/2-0.5),
        float(L/4),
        0.1
    )

    if st.button("Simulate Fence"):

        with col2:

            y=(L-2*x)/3

            fig2,ax2=plt.subplots(figsize=(6,4))

            # RECTÁNGULO EXTERIOR
            rect_x=[0,x,x,0,0]
            rect_y=[0,0,y,y,0]

            ax2.plot(rect_x,rect_y,linewidth=3)

            # CERCA INTERNA
            ax2.plot([x/2,x/2],[0,y],linewidth=3)

            ax2.set_aspect('equal')
            ax2.set_xlim(-1,x*1.4)
            ax2.set_ylim(-1,y*1.4)

            ax2.set_title("Geometry with Internal Fence")

            st.pyplot(fig2)

            st.success(f"Area = {x*y:.2f} m²")
