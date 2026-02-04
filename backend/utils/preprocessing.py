from PIL import Image #used for image loading and processing
import torchvision.transforms as transforms #used for image transformations, standard image preparation steps

def preprocess_image(path: str): #define a function to preprocess an image given its file path, #output is a tensor suitable for model input
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
