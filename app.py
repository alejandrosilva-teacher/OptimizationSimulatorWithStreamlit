import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(layout="wide")

st.title("Quadratic Optimization Simulator")

problem = st.sidebar.selectbox(
    "Choose problem",
    ["Rectangle inside a circle",
     "Rectangle with internal fence"]
)

# ======================================================
# PROBLEMA 1 — RECTÁNGULO EN CÍRCULO
# ======================================================

if problem == "Rectangle inside a circle":

    R = st.sidebar.slider("Circle radius",2.0,10.0,5.0)

    x = st.slider(
        "Control parameter x",
        0.2,
        float(R-0.2),
        float(R/2),
        key="circle_slider"
    )

    play = st.button("▶ Play Animation")

    placeholder = st.empty()

    def draw_scene(x):

        y=np.sqrt(R**2-x**2)

        x_vals=np.linspace(0.01,R,400)
        area_curve=4*x_vals*np.sqrt(R**2-x_vals**2)

        col1,col2=placeholder.columns(2)

        # PARÁBOLA
        with col1:
            fig1,ax1=plt.subplots(figsize=(6,4))
            ax1.plot(x_vals,area_curve)
            ax1.scatter(x,4*x*y,s=80)
            ax1.set_title("Area function")
            ax1.set_xlabel("x")
            ax1.set_ylabel("Area")
            st.pyplot(fig1)
            plt.close(fig1)

        # GEOMETRÍA
        with col2:
            fig2,ax2=plt.subplots(figsize=(6,4))

            theta=np.linspace(0,2*np.pi,400)
            ax2.plot(R*np.cos(theta),R*np.sin(theta))

            rect_x=[-x,x,x,-x,-x]
            rect_y=[-y,-y,y,y,-y]

            ax2.plot(rect_x,rect_y,linewidth=3)

            ax2.set_aspect('equal')
            ax2.set_xlim(-R*1.2,R*1.2)
            ax2.set_ylim(-R*1.2,R*1.2)

            st.pyplot(fig2)
            plt.close(fig2)

    # DIBUJO NORMAL
    draw_scene(x)

    # ANIMACIÓN
    if play:
        for val in np.linspace(0.3,R-0.3,60):
            draw_scene(val)
            time.sleep(0.05)

# ======================================================
# PROBLEMA 2 — CERCA CON DIVISIÓN INTERNA
# ======================================================

if problem == "Rectangle with internal fence":

    L = st.sidebar.slider(
        "Total fence length",
        20.0,
        120.0,
        60.0
    )

    x = st.slider(
        "Rectangle width x",
        0.5,
        float(L/2-0.5),
        float(L/4),
        key="fence_slider"
    )

    play = st.button("▶ Play Animation ")

    placeholder = st.empty()

    def draw_fence(x):

        y=(L-2*x)/3

        x_vals=np.linspace(0.1,L/2,400)
        area_curve=x_vals*(L-2*x_vals)/3

        col1,col2=placeholder.columns(2)

        # PARÁBOLA
        with col1:
            fig1,ax1=plt.subplots(figsize=(6,4))
            ax1.plot(x_vals,area_curve)
            ax1.scatter(x,x*y,s=80)
            ax1.set_title("Area function")
            ax1.set_xlabel("x")
            ax1.set_ylabel("Area")
            st.pyplot(fig1)
            plt.close(fig1)

        # GEOMETRÍA
        with col2:
            fig2,ax2=plt.subplots(figsize=(6,4))

            rect_x=[0,x,x,0,0]
            rect_y=[0,0,y,y,0]

            ax2.plot(rect_x,rect_y,linewidth=3)

            # división interna
            ax2.plot([x/2,x/2],[0,y],linewidth=3)

            ax2.set_aspect('equal')
            ax2.set_xlim(-1,x*1.4)
            ax2.set_ylim(-1,y*1.4)

            st.pyplot(fig2)
            plt.close(fig2)

    # DIBUJO NORMAL
    draw_fence(x)

    # ANIMACIÓN AUTOMÁTICA
    if play:
        for val in np.linspace(1,L/2-1,60):
            draw_fence(val)
            time.sleep(0.05)
