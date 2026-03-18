---
title: Face Blurrer
emoji: 🏢
colorFrom: blue
colorTo: pink
sdk: gradio
sdk_version: 5.44.1
app_file: app.py
pinned: false
short_description: 'upload a video to automatically detect and censor faces '
---

# 🎬 Video Face Blurrer

A Gradio-based web application that automatically detects and censors faces in uploaded videos using the SCRFD model (via InsightFace) and applies a smooth median blur.

## Features

- **Automated Face Detection**: Uses the robust InsightFace SCRFD model for high-accuracy face tracking.
- **Privacy-Preserving**: Automatically applies a median blur to all detected faces, ensuring privacy for subjects within the video.
- **Easy-to-use Interface**: Simply upload your `.mp4`, `.avi`, or other standard video files to the Gradio web UI and get a processed video back.
- **Cloud/Hugging Face Spaces Ready**: Deploys seamlessly on Hugging Face Spaces or other environments supporting Gradio.

## How it Works

1. **Upload**: Users upload a video through the Gradio web interface.
2. **Processing**: The backend uses OpenCV to process the video frame-by-frame. The InsightFace model detects bounding boxes around faces.
3. **Censoring**: A median blur is applied specifically to the bounding box regions.
4. **Output**: The processed video fragments are compiled and output as a playable `.mp4` file directly in the browser.

## Running Locally

### Prerequisites

You need Python 3.8+ installed.

### Installation

1. Clone the repository and navigate into the `face-blurrer` directory.
2. Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

### Usage

Run the app from the terminal:

```bash
python app.py
```

Then open the provided local URL (usually `http://127.0.0.1:7860`) in your browser.

## Built With

- **[Gradio](https://gradio.app/)**: Web interface.
- **[InsightFace](https://github.com/deepinsight/insightface)**: Highly-accurate SCRFD face detection model.
- **[OpenCV](https://opencv.org/)**: Video processing and blurring filter.
