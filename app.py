import gradio as gr
import cv2
import insightface
import os

# --- 1. Load the Model (ONCE) ---
print("Loading face detection model...")
app_model = insightface.app.FaceAnalysis()
app_model.prepare(ctx_id=-1, det_size=(640, 640))
print("Model loaded successfully.")

# --- 2. Create the Main Processing Function with Gradio Progress ---
def blur_video(input_video_path):
    # Define a temporary output path for the initial processing
    temp_output_path = "temp_output_video.avi"

    cap = cv2.VideoCapture(input_video_path)
    if not cap.isOpened():
        raise gr.Error("Error: Could not open the uploaded video file.")

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if total_frames == 0:
        raise gr.Error("Error: The video file appears to be empty or corrupted.")

    fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    writer = cv2.VideoWriter(temp_output_path, fourcc, fps, (frame_width, frame_height))

    for i in range(total_frames):
        ret, frame = cap.read()
        if not ret:
            break

        faces = app_model.get(frame)
        
        for face in faces:
            box = face.bbox.astype(int)
            x1, y1, x2, y2 = box[0], box[1], box[2], box[3]
            
            if x1 < 0: x1 = 0
            if y1 < 0: y1 = 0

            face_roi = frame[y1:y2, x1:x2]
            
            if face_roi.size > 0:
                blurred_face = cv2.medianBlur(face_roi, 27)
                frame[y1:y2, x1:x2] = blurred_face

        writer.write(frame)

    cap.release()
    writer.release()
    
    # Return the path to the processed video for Gradio to handle
    return temp_output_path

# --- 3. Create and Launch the Gradio Interface ---
if __name__ == "__main__":
    iface = gr.Interface(
        fn=blur_video,
        inputs=gr.Video(label="Upload Your Video"),
        # Add format="mp4" to make the output video playable in the browser
        outputs=gr.Video(label="Result", format="mp4"),
        title="🎬 Video Face Blurrer",
        description="Upload a video to automatically detect and censor faces using the SCRFD model and a smooth Median Blur."
    )
    
    iface.launch()