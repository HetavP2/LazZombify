# LazZombify

## Introduction

LazZombify is a Python-based computer vision project that demonstrates real-time face detection using your webcam. Leveraging OpenCV and Haar cascades, it highlights detected faces in a live video stream. The project is beginner-friendly and serves as a practical introduction to image processing and face recognition techniques.

---

## ✨ Features

- **Real-Time Face Detection**
  - Detects faces from webcam feed using Haar cascade classifier.
  - Draws rectangles around detected faces in the video stream.

- **Simple User Interaction**
  - Press `q` to quit the application.
  - Easy-to-understand code for learning and experimentation.

- **Extensible Scripts**
  - Includes additional scripts (e.g., `zombie.py`) for further image processing or experimentation.

- **Open Source References**
  - Uses publicly available Haar cascade data and tutorials.

---

## 🛠️ Tech Stack

- **Backend / Core**
  - **Python 3.x**
  - **OpenCV (`cv2`)**: For image capture and face detection.
  - **NumPy**: For array and image data manipulation.

- **Data**
  - **Haar Cascade XML**: Pre-trained classifier for frontal face detection.

---

## 📝 Project Structure

- `firsttolearnfacerec.py` — Main script for face detection.
- `haarcascade_frontalface_default.xml` — Haar cascade classifier file.
- `zombie.py` — Additional image processing script.
- `sources.txt` — References and data sources.

---

## How to Run

Follow these steps to set up and run LazZombify:

1. **Install Python**  
   Ensure Python 3.x is installed on your system.

2. **Install dependencies**  
   Open a terminal in the project directory and run:
   ```
   pip install opencv-python numpy
   ```

3. **Run the application**  
   In the project directory, execute:
   ```
   python firsttolearnfacerec.py
   ```

4. **Access the face detection window**  
   A window titled "Zombie Detection" will open, showing your webcam feed with rectangles around detected faces.  
   Press `q` to quit.

---

## References

See `sources.txt` for tutorials and data sources:
- [YouTube Tutorial](https://www.youtube.com/watch?v=i3sLv1sus0I)
- [GeeksforGeeks Color Detection](https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/)
- [OpenCV Haarcascade](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)
