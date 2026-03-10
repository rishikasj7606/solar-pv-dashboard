import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Function to calculate the PV system requirements
def calculate_system_requirements(load_energy, max_load, sunshine_hours, panel_rating, battery_efficiency, controller_efficiency):
    inverter_capacity = max_load * 1.25  # Adding safety margin
    battery_bank_capacity = load_energy / (24 * 0.7 * battery_efficiency)  # Considering depth of discharge (70%)
    pv_energy_needed = load_energy / (battery_efficiency * controller_efficiency)  # Energy required from PV
    panels_needed = np.ceil(pv_energy_needed / (sunshine_hours * panel_rating))  # Calculate number of panels

    return inverter_capacity, battery_bank_capacity, panels_needed

# Define Streamlit layout
st.title("Rooftop Solar PV System Design")

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
load_energy = st.sidebar.number_input("Daily Energy Requirement (Wh)", min_value=0, value=3800)
max_load = st.sidebar.number_input("Maximum Load (W)", min_value=0, value=875)
sunshine_hours = st.sidebar.number_input("Sunshine Hours per Day", min_value=0, value=5)
panel_rating = st.sidebar.number_input("Panel Rating (W)", min_value=0, value=80)
battery_efficiency = st.sidebar.slider("Battery Efficiency (%)", 0, 100, 85)
controller_efficiency = st.sidebar.slider("Controller Efficiency (%)", 0, 100, 95)

# Calculate system requirements
inverter_capacity, battery_bank_capacity, panels_needed = calculate_system_requirements(
    load_energy, max_load, sunshine_hours, panel_rating, battery_efficiency / 100, controller_efficiency / 100
)

# Display results
st.header("System Design Results")
st.write(f"Inverter Capacity: {inverter_capacity:.2f} kW")
st.write(f"Battery Bank Capacity: {battery_bank_capacity:.2f} Ah")
st.write(f"Number of Panels Required: {int(panels_needed)} panels")

# Energy Efficiency Visualization
fig, ax = plt.subplots()
ax.bar(['Inverter Capacity', 'Battery Capacity', 'Panels Required'], [inverter_capacity, battery_bank_capacity, panels_needed])
ax.set_ylabel("Values")
ax.set_title("Required System Components")
st.pyplot(fig)

st.write("### Design Summary")
st.write("This system is designed to meet the daily energy requirement while factoring in efficiency and safety margins. The dashboard helps users calculate necessary components such as inverter capacity, battery bank, and number of panels needed based on their usage patterns and system parameters.")
