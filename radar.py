import streamlit as st
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

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

# Random coordinates for the airplane
# Use st.session_state to keep the plane's position consistent across reruns
if 'x' not in st.session_state:
    st.session_state.x = random.randint(-900, 900)
    st.session_state.y = random.randint(-900, 900)

x = st.session_state.x
y = st.session_state.y

# Create a figure and axis
fig, ax = plt.subplots(figsize=(7, 7))  # Use subplots for better control

# Create a circle for the radar scan
circle = plt.Circle((0, 0), 0, color='blue', fill=False, linewidth=2)
ax.add_patch(circle)

# Plot the airplane and detection point
plane = ax.plot(x, y, 'ro', markersize=10, label='Airplane')[0]  # Red circle for the airplane
detected = ax.plot([], [], 'go', markersize=10, label='Detected')[0]  # Green circle for detected position

# Set the limits and labels for the plot
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_title('Radar Scan')
ax.legend(loc='lower left')

# Variable to track detection status for the animation
detection_status = {'detected_plane': False, 'detection_frame': None}


# Update function for the animation
def update(frame):
    """Updates the radar circle and checks for airplane detection."""
    radius = frame * 20  # Increase radius slightly slower for better visibility

    # Check if the airplane is within radar range
    dist_squared = x ** 2 + y ** 2

    # Only check for detection if it hasn't been detected yet
    if not detection_status['detected_plane'] and dist_squared <= (radius) ** 2:
        detected.set_data([x], [y])
        detection_status['detected_plane'] = True
        detection_status['detection_frame'] = frame
        st.sidebar.success(f"✈️ **Detected!** Position: ({x}, {y})")

    # Keep the green dot if detected, clear it if not detected and scan hasn't reached it
    elif detection_status['detected_plane']:
        detected.set_data([x], [y])
    else:
        detected.set_data([], [])

    circle.set_radius(radius)

    # Add a marker to show the current scan radius in the sidebar
    if frame % 5 == 0:
        st.sidebar.markdown(f"Current Scan Radius: **{radius:.0f}m**")

    return circle, detected


# --- Animation Setup and Display ---

# Use a button to regenerate the animation with a new position
if st.button("New Airplane Position"):
    # Clear the session state to get new random coordinates
    del st.session_state.x
    del st.session_state.y
    st.experimental_rerun()  # Rerun the app to generate new coordinates

# Sidebar for status
st.sidebar.header("Status")

# Check if the animation file exists before trying to create it every time
animation_filename = 'radar_animation.gif'

if not os.path.exists(animation_filename):
    with st.spinner('Generating radar simulation animation...'):
        # Set up the animation
        # frames=50 for a quicker, smaller GIF
        ani = FuncAnimation(fig, update, frames=50, interval=200, blit=True, repeat=False)

        # Save the animation as a GIF file
        # 'imagemagick' writer is often needed for GIF
        try:
            ani.save(animation_filename, writer='pillow', fps=10)  # 'pillow' is more common in server environments
        except Exception as e:
            st.error(f"Could not save GIF. Error: {e}")
            st.warning("You might need to install 'imagemagick' or use 'ffmpeg' as a writer.")

# Display the generated GIF
if os.path.exists(animation_filename):
    st.image(animation_filename)
    st.caption(f"Airplane at: **({x}, {y})**")

# Display the initial plane position in the sidebar
st.sidebar.markdown(f"**Airplane Position:** ({x}, {y})")

# Clear the Matplotlib figure to free memory
plt.close(fig)
