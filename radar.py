# matplotlib is a library, (pyplot and animation) are modules, pyplot containing functions
# like plot(), subplot(),...FuncAnimation is a class that defines different types of animation
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Random coordinates for the airplane
x = random.randint(-1000, 1000)
y = random.randint(-1000, 1000)

# Create a figure and axis
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)  # Create a single subplot

# Create a circle for the radar scan
circle = plt.Circle((0, 0), 0, color='blue', fill=False)
ax.add_patch(circle)

# Plot the airplane and detection point
plane = ax.plot(x, y, 'ro', markersize=10)[0]  # Red circle for the airplane
detected = ax.plot([], [], 'go', markersize=10)[0]  # Green circle for detected position

# Set the limits for the plot
ax.set_xlim(-1000, 1000)
ax.set_ylim(-1000, 1000)
ax.set_aspect('equal')  # Keep the aspect ratio square
plt.title('Radar Simulation: Detecting an Airplane')
plt.xlabel('X (m)')
plt.ylabel('Y (m)')

# Variable to track detection status
detected_plane = False

# Update function for the animation
def update(frame):
    global detected_plane
    radius = frame * 30  # Increase radius over time

    # Check if the airplane is within radar range
    dist_squared = (x - 0) ** 2 + (y - 0) ** 2  # Calculate squared distance
    if not detected_plane and dist_squared <= (radius) ** 2:  # Check that aeroplane has not been detected yet
        # and plane within radar range
        detected.set_data([x], [y])  # Set detected position
        print(f"Airplane detected at position: ({x}, {y})")  # Print position
        detected_plane = True  # Mark as detected
    else:
        #if plane is not detected within radar range
        detected.set_data([], [])  # Clear detected position if out of range

    circle.set_radius(radius)  # Update the radar circle's radius

    return circle, detected  # Return the updated objects

# Set up the animation
ani = FuncAnimation(fig, update, frames=100, interval=100)

plt.show()  # Display the plot