📸 Image Caption Generator

A modern image captioning application built using BLIP (Bootstrapped Language-Image Pre-training) and Streamlit.
Upload an image → the model intelligently generates a natural, descriptive caption.

🎯 Overview

This project generates high-quality captions for images using the Salesforce BLIP pretrained model.
The application provides a clean UI, recent history panel, and stores AI-generated outputs.

🚀 Features

Upload any image and get an instant caption
AI model: BLIP image captioning base
Clean and modern Streamlit interface
Recent captions panel (up to 50 items)
Delete recent items
Automatically saves output images to artifacts/outputs/
Centered caption below each generated output
Fast and efficient — no training needed

📂 Folder Structure

Image-Caption-Generator/
│
├── app.py
├── README.md
├── requirements.txt
├── .gitignore
│
└── artifacts/
      ├── outputs/
      │     ├── output_*.png
      └── upload/
