import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ---------------------------
# CONFIGURACIÓN GENERAL
# ---------------------------

st.set_page_config(layout="wide")
st.title("Optimization Simulator")

# Selector de problema
problem = st.sidebar.selectbox(
    "Choose optimization problem:",
    ["Rectangle inside a circle", "Rectangle with fixed fence"]
)

# =====================================================
# PROBLEMA 1 — RECTÁNGULO INSCRITO EN UN CÍRCULO
# =====================================================

if problem == "Rectangle inside a circle":

    st.header("Rectangle Inscribed in a Circle")

    # Restricción modificable
    R = st.sidebar.number_input(
        "Circle radius",
        min_value=1.0,
        value=5.0,
        step=0.5
    )

    # Modelo matemático
    x_vals = np.linspace(-R, R, 400)
    area = 4 * x_vals * np.sqrt(R**2 - x_vals**2)

    # Layout horizontal
    col1, col2 = st.columns(2)

    # ---------------- PARÁBOLA DEL ÁREA ----------------
    with col1:

        fig1, ax1 = plt.subplots(figsize=(8,4))

        ax1.plot(x_vals, area)
        ax1.set_title("Area function")
        ax1.set_xlabel("x")
        ax1.set_ylabel("Area")

        st.pyplot(fig1)

        st.latex(r"A(x)=4x\sqrt{R^2-x^2}")

    # ---------------- SLIDER ----------------
    x = st.slider(
        "Move rectangle position",
        min_value=float(0.1),
        max_value=float(R-0.1),
        value=float(R/2),
        step=0.05
    )

    # ---------------- FIGURA GEOMÉTRICA ----------------
    with col2:

        y = np.sqrt(R**2 - x**2)

        fig2, ax2 = plt.subplots(figsize=(8,4))

        theta = np.linspace(0,2*np.pi,400)
        ax2.plot(R*np.cos(theta), R*np.sin(theta))

        rect_x = [-x,x,x,-x,-x]
        rect_y = [-y,-y,y,y,-y]
        ax2.plot(rect_x, rect_y)

        ax2.set_aspect("equal")
        ax2.set_title("Geometric representation")

        st.pyplot(fig2)

        st.write(f"Area = {4*x*y:.2f}")

# =====================================================
# PROBLEMA 2 — RECTÁNGULO CON CERCA FIJA
# =====================================================

if problem == "Rectangle with fixed fence":

    st.header("Maximum Area Rectangle with Fixed Fence")

    # Restricción modificable
    L = st.sidebar.number_input(
        "Available fence length (meters)",
        min_value=4.0,
        value=40.0,
        step=2.0
    )

    x_vals = np.linspace(0.1, L/2, 400)
    area = x_vals * (L/2 - x_vals)

    col1, col2 = st.columns(2)

    # ---------------- PARÁBOLA ----------------
    with col1:

        fig1, ax1 = plt.subplots(figsize=(8,4))

        ax1.plot(x_vals, area)
        ax1.set_title("Area function")
        ax1.set_xlabel("Width (x)")
        ax1.set_ylabel("Area")

        st.pyplot(fig1)

        st.latex(r"A(x)=x\left(\frac{L}{2}-x\right)")

    # ---------------- SLIDER ----------------
    x = st.slider(
        "Rectangle width",
        min_value=float(0.5),
        max_value=float(L/2 - 0.5),
        value=float(L/4),
        step=0.1
    )

    # ---------------- FIGURA ----------------
    with col2:

        y = L/2 - x

        fig2, ax2 = plt.subplots(figsize=(8,4))

        rect_x = [0,x,x,0,0]
        rect_y = [0,0,y,y,0]
        ax2.plot(rect_x, rect_y)

        ax2.set_aspect("equal")
        ax2.set_title("Geometric representation")

        st.pyplot(fig2)

        st.write(f"Area = {x*y:.2f} m²")
