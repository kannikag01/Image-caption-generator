import streamlit as stm
from PIL import Image, ImageDraw, ImageFont
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
import os
from datetime import datetime

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

# ---------------- SAVE OUTPUT (ONE SMALL IMAGE) ---------------- #
def save_output(image, caption):
    save_dir = "artifacts/outputs"
    os.makedirs(save_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"{save_dir}/output_{timestamp}.png"

    # Convert to RGB
    img = image.convert("RGB")

    # Resize original to smaller width
    max_width = 600  # smaller output width
    w_percent = (max_width / float(img.size[0]))
    new_height = int((float(img.size[1]) * w_percent))
    img = img.resize((max_width, new_height), Image.LANCZOS)

    # Create white canvas for caption
    caption_space = 55
    final_img = Image.new("RGB", (max_width, new_height + caption_space), color="black")
    final_img.paste(img, (0, 0))

    draw = ImageDraw.Draw(final_img)

    # Load font
    try:
        font = ImageFont.truetype("arial.ttf", 24)
    except:
        font = ImageFont.load_default()

    clean_caption = caption.strip()

    # Wrap caption text
    words = clean_caption.split()
    lines = []
    line = ""

    
    for word in words:
        test_line = line + word + " "
        if draw.textlength(test_line, font=font) < (max_width - 90):
            line = test_line
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)

    # Draw caption
    y = new_height + 10
    for line in lines:
        draw.text((20, y), line, font=font, fill="white")
        y += 30

    # Save final image
    final_img.save(output_path)
    return output_path


# ---------------- SESSION STATE ---------------- #
if "history" not in stm.session_state:
    stm.session_state.history = []  

if "selected_history" not in stm.session_state:
    stm.session_state.selected_history = None

# ---------------- SIDEBAR RECENT ITEMS ---------------- #
stm.sidebar.title("Recent Captions ")

if len(stm.session_state.history) == 0:
    stm.sidebar.info("No recent captions yet.")
else:
    for i, item in enumerate(stm.session_state.history):
        thumb = item["image"].resize((120, 120))

        with stm.sidebar.container():
            cols = stm.sidebar.columns([3, 7, 2])

            with cols[0]:
                stm.image(thumb, use_container_width=True)

            with cols[1]:
                preview = item["caption"][:40] + ("..." if len(item["caption"]) > 40 else "")
                if stm.button(preview, key=f"view{i}"):
                    stm.session_state.selected_history = i

            

            stm.sidebar.markdown("---")


# ---------------- MAIN PAGE ---------------- #
stm.title("Image Caption Generator")

uploaded_file = stm.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

# ---------------- VIEW SAVED HISTORY ---------------- #
if stm.session_state.selected_history is not None:
    item = stm.session_state.history[stm.session_state.selected_history]

    stm.markdown("---")
    stm.image(item["image"], caption="Saved Image", use_container_width=True)
    stm.subheader("Generated Caption:")
    stm.write(item["caption"])

# ---------------- NEW IMAGE UPLOAD ---------------- #
elif uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    with stm.spinner("Generating caption..."):
        caption = generate_caption(image)

    # Save in history
    stm.session_state.history.insert(0, {"image": image, "caption": caption})
    stm.session_state.history = stm.session_state.history[:50]

    # Save combined output file
    saved_path = save_output(image, caption)

    
    stm.image(image, caption="Uploaded Image", use_container_width=True)
    stm.subheader("Generated Caption:")
    stm.write(caption)

# ---------------- DEFAULT SCREEN ---------------- #
else:
    stm.write("Upload an image above to begin.")
