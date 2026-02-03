# Deepfake Image Detection Using Convolutional Neural Networks and Generation Pattern Analysis

This repository contains my final-year project: an image-based deepfake detection application that classifies images as real or fake and also provides a likely generation-type inference (for example: face-swapped vs fully synthetic). The goal is to build a usable, explainable tool that demonstrates model training, backend inference, and a simple user interface.

Why this matters
-----------------
Deepfakes—realistic synthetic or manipulated faces—are increasingly used in misinformation, harassment, and fraud. Automated detection tools help reduce the spread of harmful content by flagging manipulated media. This project focuses on still-image detection and a pragmatic, defensible feature: inferring the likely generation family (face-swap vs fully synthetic) rather than claiming exact attribution.

What this project does
---------------------
- Provides a React + TypeScript frontend for image upload and result display.
- Runs a Flask backend that preprocesses images and performs model inference with PyTorch.
- Uses transfer learning (EfficientNet-B0) with a 3-class output: Real / Face-swapped / Fully synthetic.
- Includes training scripts to fine-tune the model on labeled images (extracted frames from datasets such as FaceForensics++).

Repository layout
-----------------
- `frontend/` — React UI (deploy to Vercel)
- `backend/` — Flask API, preprocessing utilities, model wrapper and requirements
- `ml_models/` — training scripts and utilities (EfficientNet skeleton)
- `data/` — dataset notes and small examples (do NOT commit large datasets)
- `docs/` — setup and deployment notes (see `docs/SETUP.md`)

Quick start (development)
-------------------------
1. Activate the project virtual environment (PowerShell example):

```powershell
cd C:\Users\ELITEBOOK\is-this-real
venv\Scripts\Activate.ps1
```

2. Install backend dependencies (inside venv):

```bash
pip install -r backend/requirements.txt
```

3. Run the backend API (development):

```bash
python backend/app.py
# backend listens on http://0.0.0.0:8000
```

4. Test the analyze endpoint (replace with your image):

```bash
curl -X POST http://localhost:8000/analyze-image -F "image=@path/to/your.jpg"
```

Training (smoke test)
---------------------
Prepare a small dataset for a quick smoke run:

```
data/sample_images/real/*.jpg
data/sample_images/face_swapped/*.jpg
data/sample_images/synthetic/*.jpg
```

Run a single-epoch training pass:

```bash
python ml_models/train.py data/sample_images --epochs 1
```

This saves a model snapshot to `backend/models/model.pth`.

Datasets and classes
--------------------
Primary dataset used for model experiments: FaceForensics++ (frames extracted and treated as images). The project groups manipulation types into three classes for training and inference:

- **Class 0 — Real:** Unmanipulated images
- **Class 1 — Face-swapped deepfake:** FaceSwap / Face2Face / DeepFakes-style manipulations
- **Class 2 — Fully synthetic / heavily manipulated:** NeuralTextures and fully generated faces

Ethics and limitations
----------------------
This system provides probabilistic inferences, not legal or forensic proof. It does not identify creators, locations, or specific software used to generate an image. All results should include a clear disclaimer and be interpreted as supportive signals rather than definitive evidence.

Contact
-------
This project was created as a final-year submission. If you need help or want new features, open an issue or message me.
