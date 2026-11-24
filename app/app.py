import streamlit as st
from ultralytics import YOLO
from PIL import Image, ImageOps, UnidentifiedImageError
import numpy as np
from pathlib import Path

@st.cache_resource
def load_model(model_path):
    return YOLO(str(model_path))


# =========================
# Page Configuration
# =========================

st.set_page_config(
    page_title="RoadGuard AI",
    page_icon="🚧",
    layout="wide"
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

confidence_threshold = st.slider(
    "Confidence Threshold",
    min_value=0.10,
    max_value=0.90,
    value=0.26,
    step=0.01
)

# =========================
# Model Checkpoints
# =========================

project_root = Path(__file__).resolve().parent.parent
model_paths = {
    "Baseline": project_root / "reports" / "baseline" / "weights" / "best.pt",
    "Improved": project_root / "reports" / "improved" / "weights" / "roadguard_best.pt",
}

st.caption("Both models use the same confidence threshold.")


def show_prediction(model_name, image, threshold):
    """Run one checkpoint and display its predictions."""
    st.subheader(model_name)
    model_path = model_paths[model_name]
    if not model_path.is_file():
        st.error(f"Model weights not found: {model_path.relative_to(project_root)}")
        return

    try:
        with st.spinner(f"Analyzing with {model_name}..."):
            model = load_model(model_path)
            # PIL images are RGB; Ultralytics handles the input conversion.
            result = model(image, conf=threshold, verbose=False)[0]
    except Exception as exc:
        st.error(f"Could not run {model_name}: {exc}")
        return

    # Ultralytics plot() returns a BGR NumPy image.
    result_image = np.ascontiguousarray(result.plot()[:, :, ::-1])
    st.image(result_image, use_container_width=True)

    boxes = result.boxes
    st.markdown("**Detected Objects**")

    if boxes is None or len(boxes) == 0:
        st.info("No objects detected.")
        return

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
            unsafe_allow_html=True,
        )


# =========================
# Image Analysis
# =========================

if uploaded_file is not None:
    try:
        with Image.open(uploaded_file) as source:
            image = ImageOps.exif_transpose(source).convert("RGB")
    except (OSError, UnidentifiedImageError):
        st.error("Could not open this image. Please upload a valid JPG or PNG.")
    else:
        st.markdown(
            '<div class="result-title">🔍 Detection Results</div>',
            unsafe_allow_html=True,
        )

        left, right = st.columns(2)
        with left:
            show_prediction("Baseline", image, confidence_threshold)
        with right:
            show_prediction("Improved", image, confidence_threshold)

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
