# Radar Simulation with Streamlit

This project is an interactive web application that simulates a radar system detecting an airplane, built using Python and the **Streamlit** framework. It transforms a standard Matplotlib animation into a user-friendly, shareable web interface.

---

## Project Description

The application dynamically simulates a radar scan attempting to locate an airplane placed at a random coordinate. The simulation is displayed as a GIF within the Streamlit UI.

### Key Features:

* **Web Interface (Streamlit)**: Provides a clean, modern UI accessible via a web browser, eliminating the need for a separate Matplotlib window.
* **Dynamic Visualization**: An expanding **blue circle** represents the radar range, centered at the origin (0, 0).
* **Randomized Targets**: An airplane (the **red dot**) is placed at a new random coordinate every time the simulation is reset.
* **Detection Logic**: The core logic checks if the airplane's position falls within the expanding radar radius.
* **Visual & Console Cues**: A **green dot** appears on the plane's position upon detection, and a confirmation message is displayed in the sidebar.
* **Restart Functionality**: A **"New Airplane Position" button** allows users to instantly reset the simulation with a new random target.

---

## Installation

To run this project, you will need **Python 3** and the following libraries.

1.  Clone this repository or download the `radar.py` file.
2.  Install all necessary libraries by running the following command in your terminal:

    ```bash
    pip install streamlit matplotlib pillow
    ```

    *Note: The `pillow` library is used by Matplotlib to save the animation as a GIF, which Streamlit then displays.*

---

## Usage

The application is run directly using the Streamlit command.

1.  Navigate to the directory containing the `radar.py` file.
2.  Run the application from your terminal:

    ```bash
    streamlit run radar.py
    ```
3.  Your default web browser will automatically open to the application (typically at `http://localhost:8501`).
4.  Interact with the app by clicking the **"New Airplane Position"** button to run a new simulation.

---

## Screenshots
<img width="2559" height="631" alt="image" src="https://github.com/user-attachments/assets/d138dc5a-1722-4e9a-ba89-e269caa4a2bc" />
<img width="2559" height="1259" alt="image" src="https://github.com/user-attachments/assets/a9a826ad-9e0a-4ed6-9ed0-01cf959511c0" />
<img width="2556" height="501" alt="image" src="https://github.com/user-attachments/assets/9242e7a9-1893-4393-94f1-cbfbb17c7185" />

