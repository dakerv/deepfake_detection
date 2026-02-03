from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from werkzeug.utils import secure_filename
from backend.utils.preprocessing import preprocess_image

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/analyze-image', methods=['POST'])
def analyze_image():
    if 'image' not in request.files:
        return jsonify({'error': 'no image provided'}), 400
    f = request.files['image']
    filename = secure_filename(f.filename)
    path = os.path.join(UPLOAD_FOLDER, filename)
    f.save(path)

    # Preprocess (face crop / resize). This is a minimal stub.
    img_tensor = preprocess_image(path)

    # TODO: load model and run inference. For now return a placeholder.
    result = {
        'authenticity': 'Unknown',
        'generation_type': 'Unknown',
        'confidence': 0.0
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
