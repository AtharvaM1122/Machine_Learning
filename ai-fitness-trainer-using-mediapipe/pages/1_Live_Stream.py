import os
import sys
import cv2  # ✅ Using OpenCV instead of `av`
import streamlit as st
from streamlit_webrtc import VideoHTMLAttributes, webrtc_streamer

BASE_DIR = os.path.abspath(os.path.join(__file__, '../../'))
sys.path.append(BASE_DIR)

from utils import get_mediapipe_pose
from process_frame import ProcessFrame
from thresholds import get_thresholds_beginner, get_thresholds_pro

st.title('AI Fitness Trainer: Squats & Bicep Curl Analysis')

mode = st.radio('Select Mode', ['Beginner', 'Pro'], horizontal=True)

thresholds = get_thresholds_beginner() if mode == 'Beginner' else get_thresholds_pro()

live_process_frame = ProcessFrame(thresholds=thresholds, flip_frame=True)
pose = get_mediapipe_pose()

if 'download' not in st.session_state:
    st.session_state['download'] = False

output_video_file = f'output_live.avi'  # ✅ Changed format to .avi for OpenCV

# ✅ Use OpenCV's VideoWriter instead of `av`
video_writer = cv2.VideoWriter(output_video_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (480, 480))

def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")  # Convert frame to numpy array
    processed_img, _ = live_process_frame.process(img, pose)  # Process frame
    video_writer.write(processed_img)  # Save processed frame
    return processed_img  # Return processed frame

ctx = webrtc_streamer(
    key="Pose-Analysis",
    video_frame_callback=video_frame_callback,
    rtc_configuration={"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]},
    media_stream_constraints={"video": {"width": {'min':480, 'ideal':480}}, "audio": False},
    video_html_attrs=VideoHTMLAttributes(autoPlay=True, controls=False, muted=False),
)

# ✅ Handle video download
download_button = st.empty()

if os.path.exists(output_video_file):
    with open(output_video_file, 'rb') as op_vid:
        download = download_button.download_button('Download Video', data=op_vid, file_name='output_live.avi')

        if download:
            st.session_state['download'] = True

if os.path.exists(output_video_file) and st.session_state['download']:
    os.remove(output_video_file)
    st.session_state['download'] = False
    download_button.empty()
