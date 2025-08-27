# LazZombify

LazZombify is a Python project that performs real-time face detection using your webcam and OpenCV. It demonstrates basic computer vision techniques with Haar cascades.

## Features

- Real-time face detection via webcam
- Highlights detected faces with rectangles

## Project Structure

- `firsttolearnfacerec.py` — Main script for face detection
- `haarcascade_frontalface_default.xml` — Haar cascade classifier for faces
- `zombie.py` — Additional image processing script (see file for details)
- `sources.txt` — References and sources for code/data

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

Install dependencies:

```sh
pip install opencv-python numpy
```

## Usage

1. Ensure your webcam is connected.
2. Run the main script:

    ```sh
    python firsttolearnfacerec.py
    ```

3. A window titled "Zombie Detection" will open, showing your webcam feed with rectangles around detected faces.
4. Press `q` to quit.

## How It Works

- Loads Haar cascade classifier for face detection
- Captures frames from webcam
- Detects faces and draws rectangles
- Displays the processed video feed

## References

See `sources.txt` for tutorials and data sources:
- [YouTube Tutorial](https://www.youtube.com/watch?v=i3sLv1sus0I)
- [GeeksforGeeks Color Detection](https://www.geeksforgeeks.org/multiple-color-detection-in-real-time-using-python-opencv/)
- [OpenCV Haarcascade](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)
