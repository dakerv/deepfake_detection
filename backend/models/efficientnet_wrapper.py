import torch
import os
from torchvision import models

class EfficientNetWrapper:
    def __init__(self, model_path: str = None, device: str = 'cpu'):
        self.device = torch.device(device)
        self.model = models.efficientnet_b0(pretrained=True)
        # Replace classifier head for 3 classes
        num_features = self.model.classifier[1].in_features
        self.model.classifier = torch.nn.Sequential(
            torch.nn.Dropout(0.2),
            torch.nn.Linear(num_features, 3)
        )
        if model_path and os.path.exists(model_path):
            self.model.load_state_dict(torch.load(model_path, map_location=self.device))
        self.model.to(self.device)
        self.model.eval()

    def predict(self, tensor):
        # tensor: single image tensor [3, H, W]
        with torch.no_grad():
            x = tensor.unsqueeze(0).to(self.device)
            logits = self.model(x)
            probs = torch.nn.functional.softmax(logits, dim=1)[0].cpu().tolist()
        return probs
