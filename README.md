# Radar Simulation

This project is a simple Python program that simulates a radar system detecting an airplane. It's an excellent demonstration of using Python for real-time data visualization and simulation.

---

### Project Description

The program uses the **Matplotlib** library to create a dynamic simulation. It generates a random location for an airplane and then animates a radar scan by growing a circle from the origin. The simulation checks for the airplane's position in each frame.

Key features include:
* **Dynamic Visualization**: Utilizes `matplotlib.animation.FuncAnimation` to create a continuous, frame-by-frame simulation.
* **Randomized Targets**: The airplane's position is randomized for a new simulation experience each time the program is run.
* **Detection Logic**: The program's core logic is to check if the airplane's coordinates fall within the expanding radar radius.
* **Visual Cues**: The simulation provides clear visual feedback—a red dot for the airplane, a growing blue circle for the radar, and a green dot that appears when the plane is detected.

---

### Installation

To run this program, you will need to have Python 3 installed on your system. You also need the required Matplotlib library, which can be installed via pip.

1.  Clone this repository or download the `radar.py` file.
2.  Install the necessary library by running the following command in your terminal:
    ```bash
    pip install matplotlib
    ```

---

### Usage

1.  Navigate to the directory containing the `radar.py` file.
2.  Run the program from your terminal:
    ```bash
    python radar.py
    ```
3.  The program will open a new window and begin the simulation. A message will be printed to the console when the airplane is detected.

---

### Screenshots
![Radar Simulation](radar_simulation.gif)
