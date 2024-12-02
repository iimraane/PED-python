# Daily Photo Capture - README

## Description

This Python project allows you to take a daily photo using your computer's webcam. It is a simple and quick solution that enables you to capture your appearance evolution day by day.

Photos are automatically saved in a folder named `PED`, with a filename based on the current date and time (e.g., `2024-12-02_14-30-15.jpg`).

This project is ideal for those who want to track their daily evolution in a simple way.

## Features
- Automatic photo capture with the webcam.
- Photos saved in a predefined folder (`PED`).
- Filename based on the date and time, for easy tracking.

## Dependencies
To use this project, you need to install the following libraries:
- `opencv-python`
- `numpy`

To install the dependencies, run the following command:
```sh
pip install opencv-python numpy
```

## Usage
1. Clone this project or copy the source code to your machine.
2. Ensure the dependencies are installed.
3. Simply run the Python script:
```sh
python PED.py
```

The script will open the webcam and take a photo automatically, then save it in the `PED` folder.

## Technical Details
- The script uses `OpenCV` to capture the photo from the webcam.
- If you are on Windows, the screen brightness is automatically increased to improve image quality.
- File names are generated based on the date and time to ensure each photo is unique.

## Notes
- Make sure your webcam is connected and functioning properly before running the script.
- Photos will be saved in the `PED` folder located in the same directory as the script.

## Supported Platforms
This project is compatible with Windows, Linux, and macOS. Note that screen brightness adjustment is only available on Windows.

## Author
This project was designed to capture daily moments in a simple and effective way. Enjoy seeing your evolution over time!

