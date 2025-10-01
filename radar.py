import streamlit as st
import random
import matplotlib.pyplot as plt
import time  # Import time for a slight pause to show progression

# --- Streamlit UI Setup ---
st.set_page_config(page_title="Radar Simulation", layout="centered")
st.title("Radar Simulation: Detecting an Airplane")
st.markdown("""
This app simulates a radar scan attempting to detect a randomly placed airplane.
The **blue circle** represents the expanding radar range, and the **red dot** is the airplane.
When the airplane is detected, a **green dot** appears at its position.
""")
# ---

# --- Simulation Logic ---

# Use st.session_state to keep the plane's position consistent
if 'x' not in st.session_state or 'y' not in st.session_state:
    st.session_state.x = random.randint(-900, 900)
    st.session_state.y = random.randint(-900, 900)
    st.session_state.detected = False

x = st.session_state.x
y = st.session_state.y
plane_dist_sq = x ** 2 + y ** 2

# Create a figure and axis outside the loop
fig, ax = plt.subplots(figsize=(7, 7))

# Set the limits and labels for the plot
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Radar Scan')

# Plot the airplane
ax.plot(x, y, 'ro', markersize=10, label='Airplane')

# Placeholders for dynamic plot elements
circle = plt.Circle((0, 0), 0, color='blue', fill=False, linewidth=2, label='Radar Range')
ax.add_patch(circle)
detected_plot = ax.plot([], [], 'go', markersize=10, label='Detected')[0]

# Sidebar for status
st.sidebar.header("Status")
st.sidebar.markdown(f"**Airplane Position:** ({x}, {y})")

# Placeholder for the Matplotlib plot in the app's main area
plot_area = st.empty()
status_sidebar = st.sidebar.empty()

# --- Radar Scanning Loop (Replaces FuncAnimation) ---
# Check if the scan should run (e.g., on initial load or after a new position)
if not st.session_state.detected:
    max_radius = 1450  # Max radius to ensure detection in all corners
    step = 50  # How much the radius increases per "frame"

    st.session_state.detected = False

    # Loop through the scan frames
    for radius in range(0, max_radius + step, step):
        radius_sq = radius ** 2

        # Check for detection
        if not st.session_state.detected and plane_dist_sq <= radius_sq:
            st.session_state.detected = True
            st.session_state.detection_radius = radius

            # Update the detected plot immediately
            detected_plot.set_data([x], [y])
            status_sidebar.success(f"✈️ **Detected!** Position: ({x}, {y})")

        # Update radar circle for this frame
        circle.set_radius(radius)

        # Display the current state of the plot
        plot_area.pyplot(fig)
        status_sidebar.markdown(f"Current Scan Radius: **{radius:.0f}m**")

        # Pause briefly to simulate animation progression
        time.sleep(0.1)

        # Stop the scan once detected
        if st.session_state.detected:
            break

# If detected, just show the final plot state
if st.session_state.detected:
    circle.set_radius(st.session_state.detection_radius)
    detected_plot.set_data([x], [y])
    status_sidebar.success(f"✈️ **Detected!** Position: ({x}, {y})")
    status_sidebar.markdown(f"Detection Radius: **{st.session_state.detection_radius:.0f}m**")
    plot_area.pyplot(fig)
else:
    plot_area.pyplot(fig)  # Show the final, non-detected state

# --- Button Logic ---
if st.button("New Airplane Position"):
    # Clear the session state to get new random coordinates and reset detection
    del st.session_state.x
    del st.session_state.y
    st.session_state.detected = False

    # Rerun the app to generate new coordinates and start the scan
    st.rerun()

# Clear the Matplotlib figure to free memory
plt.close(fig)
