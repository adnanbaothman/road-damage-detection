import streamlit as st
from PIL import Image
import numpy as np
from pathlib import Path
from ultralytics import YOLO

# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="RoadGuard AI",
    page_icon="🚧",
    layout="centered"
)


# =========================
# Custom CSS
# =========================

st.markdown("""
<style>

    .main-title {
        text-align: center;
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #6b7280;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .upload-title {
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 10px;
    }

    .result-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 15px;
    }

    .result-card {
        padding: 15px 20px;
        border-radius: 12px;
        border: 1px solid #e5e7eb;
        margin-bottom: 10px;
        background-color: #f9fafb;
    }

    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        margin-top: 45px;
    }

</style>
""", unsafe_allow_html=True)


# =========================
# Header
# =========================

st.markdown(
    '<div class="main-title">🚧 RoadGuard AI</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">AI-Powered Road Damage Detection</div>',
    unsafe_allow_html=True
)


# =========================
# Upload Section
# =========================

st.markdown(
    '<div class="upload-title">Upload Road Image</div>',
    unsafe_allow_html=True
)

if "uploader_key" not in st.session_state:
    st.session_state.uploader_key = 0


uploaded_file = st.file_uploader(
    "Choose an image of a road",
    type=["jpg", "jpeg", "png"],
    key=f"road_image_{st.session_state.uploader_key}"
)


# =========================
# Image Analysis
# =========================

if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    image_array = np.array(image)

    # Load trained road-damage YOLO model
    BASE_DIR = Path(__file__).resolve().parents[1]
    MODEL_PATH = BASE_DIR / "reports" / "baseline" / "weights" / "best.pt"

    model = YOLO(str(MODEL_PATH))

    # Analyze automatically
    with st.spinner("Analyzing image..."):
        results = model(image_array, conf=0.26)

    # Create detection image
    result_image = results[0].plot()

    # =========================
    # Detection Result
    # =========================

    st.markdown(
        '<div class="result-title">🔍 Detection Result</div>',
        unsafe_allow_html=True
    )

    st.image(
        result_image,
        width=600
    )


    # =========================
    # Detection Information
    # =========================

    boxes = results[0].boxes

    if boxes is not None and len(boxes) > 0:

        st.markdown(
            '<div class="result-title">📊 Detected Objects</div>',
            unsafe_allow_html=True
        )

        for box in boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = model.names[class_id]

            st.markdown(
                f"""
                <div class="result-card">
                    <strong>{class_name.title()}</strong>
                    <br>
                    Confidence: {confidence * 100:.1f}%
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info("No objects detected.")


    # =========================
    # Upload New Image
    # =========================

    st.write("")

    if st.button("🗑️ Delete Image"):

        st.session_state.uploader_key += 1
        st.rerun()


# =========================
# Footer
# =========================

st.markdown(
    '<div class="footer">RoadGuard AI • Road Damage Detection Prototype</div>',
    unsafe_allow_html=True
)