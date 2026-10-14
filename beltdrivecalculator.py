import math
import streamlit as st

st.set_page_config(
    page_title="Belt Drive Calculator",
    page_icon="⚙️",
    layout="centered"
)

st.title("⚙️ Belt Drive Calculator")
st.write("Calculate belt velocity, transmitted power, tension ratio, and torque.")

st.divider()

option = st.selectbox(
    "Select Calculation",
    [
        "Belt Velocity",
        "Power Transmitted",
        "Tension Ratio",
        "Torque Transmitted"
    ]
)

st.subheader(f"📌 {option}")

if option == "Belt Velocity":
    d = st.number_input(
        "Pulley Diameter (m)",
        min_value=0.0,
        value=0.2,
        step=0.01
    )
    n = st.number_input(
        "Rotational Speed (RPM)",
        min_value=0.0,
        value=500.0,
        step=10.0
    )

    if st.button("Calculate Velocity"):
        velocity = (math.pi * d * n) / 60
        st.success(f"Belt Velocity: {velocity:.2f} m/s")

elif option == "Power Transmitted":
    t1 = st.number_input(
        "Tight Side Tension T1 (N)",
        min_value=0.0,
        value=500.0,
        step=10.0
    )
    t2 = st.number_input(
        "Slack Side Tension T2 (N)",
        min_value=0.0,
        value=200.0,
        step=10.0
    )
    v = st.number_input(
        "Belt Velocity (m/s)",
        min_value=0.0,
        value=5.0,
        step=0.5
    )

    if st.button("Calculate Power"):
        power = (t1 - t2) * v
        st.success(f"Power Transmitted: {power:.2f} W")
        st.metric("Power in kW", f"{power / 1000:.3f} kW")

elif option == "Tension Ratio":
    t1 = st.number_input(
        "Tight Side Tension T1 (N)",
        min_value=0.0,
        value=500.0,
        step=10.0
    )
    t2 = st.number_input(
        "Slack Side Tension T2 (N)",
        min_value=0.0,
        value=200.0,
        step=10.0
    )

    if st.button("Calculate Ratio"):
        if t2 != 0:
            ratio = t1 / t2
            st.success(f"Tension Ratio (T1/T2): {ratio:.2f}")
        else:
            st.error("Slack side tension T2 must be greater than zero.")

elif option == "Torque Transmitted":
    t1 = st.number_input(
        "Tight Side Tension T1 (N)",
        min_value=0.0,
        value=500.0,
        step=10.0
    )
    t2 = st.number_input(
        "Slack Side Tension T2 (N)",
        min_value=0.0,
        value=200.0,
        step=10.0
    )
    d = st.number_input(
        "Pulley Diameter (m)",
        min_value=0.0,
        value=0.2,
        step=0.01
    )

    if st.button("Calculate Torque"):
        torque = (t1 - t2) * (d / 2)
        st.success(f"Torque Transmitted: {torque:.2f} N·m")

st.divider()
st.caption("Belt Drive Calculator | Powered by Python & Streamlit")
