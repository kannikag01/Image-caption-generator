import streamlit as stm
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

# ---------------- PAGE CONFIG ---------------- #
stm.set_page_config(
    page_title="Image Caption Generator",
    page_icon="🧊",
    layout="wide"
)

# ---------------- LOAD BLIP ---------------- #
@stm.cache_resource
def load_blip():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model

processor, model = load_blip()

# ---------------- CAPTION GENERATOR ---------------- #
def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    output = model.generate(**inputs, max_length=60)
    caption = processor.decode(output[0], skip_special_tokens=True)
    return caption.capitalize()

# ---------------- SESSION HISTORY ---------------- #
if "history" not in stm.session_state:
    stm.session_state.history = []  # stores {"image": image, "caption": caption}

if "selected_history" not in stm.session_state:
    stm.session_state.selected_history = None

# ---------------- SIDEBAR : RECENTS ---------------- #
stm.sidebar.title("🕒 Recent Captions (Max 50)")

if len(stm.session_state.history) == 0:
    stm.sidebar.info("No recent captions yet.")
else:
    for i, item in enumerate(stm.session_state.history):

        thumb = item["image"].resize((120, 120))   # BETTER THUMBNAIL

        with stm.sidebar.container():
            cols = stm.sidebar.columns([3, 7, 2])

            # Thumbnail
            with cols[0]:
                stm.image(thumb, use_container_width=True)

            # Caption preview
            with cols[1]:
                preview = item["caption"][:40] + ("..." if len(item["caption"]) > 40 else "")
                if stm.button(preview, key=f"view{i}"):
                    stm.session_state.selected_history = i

            # Delete
            

# ---------------- MAIN PAGE ---------------- #
stm.title("AI Image Caption Generator")

# Centered uploader
uploaded_file = stm.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# ---------------- VIEW FROM HISTORY ---------------- #
if stm.session_state.selected_history is not None:
    item = stm.session_state.history[stm.session_state.selected_history]

    stm.markdown("---")
    stm.image(item["image"], caption="Saved Image", use_container_width=True)
    stm.subheader("Generated Caption:")
    stm.write(item["caption"])

# ---------------- NEW UPLOAD ---------------- #
elif uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    with stm.spinner("Generating caption..."):
        caption = generate_caption(image)

    # Save history (max 50)
    stm.session_state.history.insert(0, {"image": image, "caption": caption})
    stm.session_state.history = stm.session_state.history[:50]

    # Show image and caption (caption BELOW image)
    stm.image(image, caption="Uploaded Image", use_container_width=True)
    stm.subheader("Generated Caption:")
    stm.write(caption)

# ---------------- DEFAULT SCREEN ---------------- #
else:
    stm.write("Upload an image above to begin.")
