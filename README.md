

📸 Image Caption Generator

An  application that generates intelligent and meaningful captions for images using the BLIP (Bootstrapped Language-Image Pre-training) model and a modern Streamlit user interface.


🎯 Overview

This project uses Salesforce BLIP, a state-of-the-art image-captioning model, to generate accurate and natural captions.
Simply upload an image, and the application instantly generates a caption and also saves an output image with the caption attached.

The app also includes a recent history panel, saving up to 50 recent outputs with delete support.

🚀 Features

✔ Upload any image
✔ AI-generated descriptive captions
✔ Clean UI with centered captions
✔ Auto-save outputs into artifacts/outputs/
✔ Recent history 
✔ Delete history items
✔ Modern design
✔ No training required — uses a pretrained BLIP model
✔ Works offline once model is downloaded



📂 Project Structure
Image-Caption-Generator/
│
├── app.py                  # Main Streamlit application
├── README.md               # Documentation
├── requirements.txt        # Dependencies
├── .gitignore              # Git ignore rules
│
└── artifacts/
    ├── outputs/            # Saved captioned images
    └── upload/             # Uploaded images (temporary)

🔧 Installation
1️⃣ Clone the repository
git clone https://github.com/kannikag01/Image-caption-generator.git
cd Image-caption-generator

2️⃣ Create a virtual environment
python -m venv venv

3️⃣ Activate the environment

Windows:

venv\Scripts\activate


Linux/Mac:

source venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

▶️ Run the App
streamlit run app.py


The app will open automatically or you can visit:

http://localhost:8501/

💾 Saved Outputs

Every captioned image is saved automatically as:

artifacts/outputs/output_YYYYMMDD_HHMMSS.png


Each saved file contains:

The resized original image

A centered, clean caption

White background with neat formatting

🧠 Model Used
✔ BLIP — Salesforce/blip-image-captioning-base

Transformer-based encoder–decoder

High-quality multilingual captioning

Works offline afterwards

State-of-the-art architecture

🛠 Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
AI Model	BLIP (Transformers, PyTorch)
Image Processing	Pillow
Storage	artifacts/outputs
👩‍💻 Author

Kannika G
AI Developer & Software Engineer

📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this software.

🚧 Future Enhancements

 Add image drag-and-drop support

 Add dark/light theme switch

 Add multiple captioning models (BLIP-2, GIT, etc.)

 Add download button for output image

 Add API version for developers