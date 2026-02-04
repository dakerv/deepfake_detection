from PIL import Image #used for image loading and processing
import torchvision.transforms as transforms #used for image transformations, standard image preparation steps

def preprocess_image(path: str): #define a function to preprocess an image given its file path, #output is a tensor suitable for model input
    """Minimal preprocessing: load image, convert to RGB, resize to 224x224 and return tensor-compatible PIL image.
    Replace with face-detection + alignment later.
    """
    img = Image.open(path).convert('RGB') #opens image and forces into RGB format, some images are grayscale, CMYK, #CNNs expect 3 channels (R,G,B)
    transform = transforms.Compose([
        transforms.Resize((224, 224)), #resize image to 224x224 pixels, EfficientNetB0 expects this input size
        transforms.ToTensor(), #convert image to PyTorch tensor, scales pixel values to [0,1] from [0,255], #and rearranges dimensions to [C, H, W] (channels, height, width)
    ])
    tensor = transform(img)
    # Return a CPU tensor; model wrapper will handle batches
    return tensor
