


Image Caption Generator
````markdown
An image captioning app that uses Salesforce BLIP to generate natural image captions
and a modern Streamlit UI to upload images, generate captions, and save captioned outputs.

 Features

 Single-file Streamlit app (`app.py`) for local or cloud use.  
 Uses the BLIP image-captioning model for high-quality captions.  
 Auto-saves captioned outputs to `artifacts/outputs/`.  
 Keeps a recent history panel .  
 No training required uses pretrained BLIP weights.  
 Works offline after model weights are cached.
````


Quick start
```bash
Recommended: use Python 3.10 or 3.11.
````

1. Clone the repository
```bash
git clone https://github.com/kannikag01/Image-caption-generator.git
cd Image-caption-generator
````

2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

> **GPU note for `torch`**: If you want GPU acceleration, install `torch` following the official instructions for your CUDA version (see [https://pytorch.org/get-started/locally/](https://pytorch.org/get-started/locally/)) — for example:

```bash
# example for CUDA 11.8 (replace with your cuda version if needed)
pip install torch torchvision --index-url https://download.pytorch.org/whl/cu118
```

4. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) if Streamlit doesn't open automatically.



 Usage

1. Upload an image (JPEG/PNG).
2. App runs BLIP and shows a generated caption.
3. Click the UI controls to save / clear / manage recent history.
4. Saved outputs are stored under `artifacts/outputs/output_YYYYMMDD_HHMMSS.png`.



Project structure

```
Image-caption-generator/
├── app.py                 # Main Streamlit application
├── inspect_model.py       # Optional: model inspect utilities
├── requirements.txt       # Python dependencies
├── README.md
├── .gitignore
└── artifacts/
    ├── outputs/           # Saved captioned images
    └── upload/            # Temporary uploads (used by app)
```

---

 Recommended `requirements.txt`

> Use the `requirements.txt` below (versions chosen to be stable and compatible). If you have an existing `requirements.txt`, either replace or merge versions as appropriate.

```
streamlit>=1.20.0
torch>=2.2.0
torchvision>=0.15.0
transformers>=4.34.0
accelerate>=0.20.0
huggingface-hub>=0.14.0
Pillow>=9.0.0
numpy>=1.24.0
safetensors>=0.3.0
tqdm>=4.64.0
```

> Notes:
>
> * `torch` install is platform/CUDA-specific; follow PyTorch installation instructions for best compatibility.
> * `safetensors` is optional depending on how model weights are stored/loaded — keep it if you use safetensors or HF-saved safetensors.



## Model

* Model used: `Salesforce/blip-image-captioning-base` (pretrained).
* The model weights are downloaded automatically on first run (Hugging Face cache) and then work offline.


## Deployment tips

* To deploy to Streamlit Cloud, Heroku, or a container, make sure to:

  * Add `Procfile` (for Heroku) or `streamlit` config.
  * Ensure `requirements.txt` contains the exact versions used.
  * Add any environmental variables if required (none for the current app).
* For GPU-backed deployments, pick a host with GPU support and install `torch` with the proper CUDA wheel.



## Troubleshooting

* **Model import errors**: Ensure `torch` and `transformers` are installed and compatible. Reinstall `torch` for your CUDA version if necessary.
* **Large wheel / slow installs**: Install `torch` using the official PyTorch instructions for performance and compatibility.
* **Permission errors while saving**: Ensure the `artifacts/outputs/` folder exists and is writable. Create it manually if needed:

  ```bash
  mkdir -p artifacts/outputs
  mkdir -p artifacts/upload
  ```
* **Streamlit port issues**: If port 8501 is blocked, use:

  ```bash
  streamlit run app.py --server.port 8502
  ```

---


## Author

Kannika G — AI Developer & Software Engineer

---

## Future improvements (suggested)

* Add drag & drop image support.
* Add download button for captioned outputs.
* Add model selection (BLIP-2, GIT) or an API server version.
* Add a small unit-test suite and CI pipeline.



