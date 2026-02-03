# Setup (Backend + ML)

1. Create and activate a Python virtual environment:

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

2. Install backend dependencies:

```bash
pip install -r backend/requirements.txt
```

3. To train (example):

```bash
python ml_models/train.py data/sample_images --epochs 1
```

4. To run the backend locally:

```bash
python backend/app.py
# The server will listen on http://0.0.0.0:8000
```
