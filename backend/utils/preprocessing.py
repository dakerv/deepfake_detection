from PIL import Image
import torchvision.transforms as transforms

def preprocess_image(path: str):
    """Minimal preprocessing: load image, convert to RGB, resize to 224x224 and return tensor-compatible PIL image.
    Replace with face-detection + alignment later.
    """
    img = Image.open(path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
    ])
    tensor = transform(img)
    # Return a CPU tensor; model wrapper will handle batches
    return tensor
