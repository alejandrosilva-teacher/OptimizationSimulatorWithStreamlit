import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")

st.title("📈 Quadratic Optimization Simulator")

option = st.sidebar.selectbox(
    "Choose Simulation",
    ["Rectangle in a Circle", "Rectangular Pens"]
)

# =====================================================
# CONTENEDORES DE DISEÑO
# =====================================================

graphs = st.container()
controls = st.container()

# =====================================================
# SIMULACIÓN 1
# =====================================================

if option == "Rectangle in a Circle":

    R = 5

    # SLIDER (lógica primero)
    x = controls.slider("Move x", 0.1, 4.9, 2.0)

    y = np.sqrt(R**2 - x**2)
    A = 4*x*y

    with graphs:

        col1, col2 = st.columns(2)

        # ---------------- PARÁBOLA ----------------
        with col1:

            st.subheader("Area Function")

            x_vals = np.linspace(0, R, 400)
            A_vals = 4*x_vals*np.sqrt(R**2 - x_vals**2)

            fig, ax = plt.subplots(figsize=(6,4))
            ax.plot(x_vals, A_vals)
            ax.plot(x, A, 'ro')
            ax.set_xlabel("x")
            ax.set_ylabel("Area")

            st.pyplot(fig)
            plt.close(fig)

        # ---------------- GEOMETRÍA ----------------
        with col2:

            st.subheader("Geometric Model")

            fig2, ax2 = plt.subplots(figsize=(6,4))

            theta = np.linspace(0,2*np.pi,400)
            ax2.plot(R*np.cos(theta), R*np.sin(theta))

            rect_x = [-x,x,x,-x,-x]
            rect_y = [-y,-y,y,y,-y]

            ax2.plot(rect_x,rect_y,linewidth=3)

            ax2.set_aspect('equal')

            st.pyplot(fig2)
            plt.close(fig2)

    st.success(f"Area = {A:.2f}")

    st.latex(r"x^2+y^2=25")
    st.latex(r"A(x)=4x\sqrt{25-x^2}")


# =====================================================
# SIMULACIÓN 2
# =====================================================

else:

    x = controls.slider("Width x", 1.0, 140.0, 50.0)

    y = (300 - 2*x)/3
    A = x*y

    with graphs:

        col1, col2 = st.columns(2)

        # -------- PARÁBOLA ----------
        with col1:

            st.subheader("Area Function")

            x_vals = np.linspace(1,140,400)
            A_vals = x_vals*(300-2*x_vals)/3

            fig, ax = plt.subplots(figsize=(6,4))
            ax.plot(x_vals, A_vals)
            ax.plot(x, A, 'ro')
            ax.set_xlabel("x")
            ax.set_ylabel("Area")

            st.pyplot(fig)
            plt.close(fig)

        # -------- GEOMETRÍA ----------
        with col2:

            st.subheader("Geometric Model")

            fig2, ax2 = plt.subplots(figsize=(6,4))

            rect_x=[0,x,x,0,0]
            rect_y=[0,0,y,y,0]

            ax2.plot(rect_x,rect_y,linewidth=3)
            ax2.plot([0,x],[y/2,y/2],linewidth=3)

            ax2.set_aspect('equal')
            ax2.set_xlim(0,x*1.2)
            ax2.set_ylim(0,y*1.2)

            st.pyplot(fig2)
            plt.close(fig2)

    st.success(f"Area = {A:.2f}")

    st.latex(r"2x+3y=300")
    st.latex(r"A(x)=100x-\frac{2}{3}x^2")
