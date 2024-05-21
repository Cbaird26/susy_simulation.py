import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('Particle Collision and SUSY Particle Detection Simulation')

# Sidebar inputs for simulation parameters
st.sidebar.header('Simulation Parameters')
num_collisions = st.sidebar.slider('Number of Collisions', 1, 1000, 100)
energy_level = st.sidebar.slider('Collision Energy Level (GeV)', 100, 10000, 1000)

# Function to simulate particle collisions
def simulate_collisions(num_collisions, energy_level):
    collisions = []
    for _ in range(num_collisions):
        particles = np.random.choice(['quark', 'gluon', 'neutralino', 'lepton'], size=10)
        energies = np.random.normal(energy_level, 100, size=10)
        collision = list(zip(particles, energies))
        collisions.append(collision)
    return collisions

# Run the simulation
collisions = simulate_collisions(num_collisions, energy_level)

# Display the results
st.write(f"Simulating {num_collisions} collisions at {energy_level} GeV energy level")
st.write("Sample of collision events:")
st.write(collisions[:5])  # Display a sample of the collision events

# Visualization of particle energy distribution
all_energies = [energy for collision in collisions for _, energy in collision]
plt.hist(all_energies, bins=30, edgecolor='black')
plt.title('Energy Distribution of Detected Particles')
plt.xlabel('Energy (GeV)')
plt.ylabel('Count')
st.pyplot(plt)

# Check for SUSY particles (neutralinos)
susy_particles = sum([1 for collision in collisions for particle, _ in collision if particle == 'neutralino'])
st.write(f"Number of SUSY particles (neutralinos) detected: {susy_particles}")
