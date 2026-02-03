import os
import sys
try:
    from torchvision import datasets, transforms
    from torch.utils.data import DataLoader
    import torch
    from torchvision import models
except Exception as e:
    print("Missing required ML packages (torch/torchvision).\nPlease run: pip install -r backend/requirements.txt", file=sys.stderr)
    raise

def train(data_dir: str, epochs: int = 1, batch_size: int = 16, lr: float = 1e-3, device: str = None):
    transform = transforms.Compose([
        transforms.Resize((224,224)),
        transforms.ToTensor()
    ])
    dataset = datasets.ImageFolder(data_dir, transform=transform)
    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    model = models.efficientnet_b0(pretrained=True)
    num_features = model.classifier[1].in_features
    model.classifier = torch.nn.Sequential(torch.nn.Dropout(0.2), torch.nn.Linear(num_features, 3))
    # choose device automatically if not provided
    if device is None:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = model.to(device)

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        running = 0.0
        for imgs, labels in loader:
            imgs = imgs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running += loss.item()
        print(f"Epoch {epoch+1}/{epochs} loss={running/len(loader):.4f}")

    os.makedirs('backend/models', exist_ok=True)
    out_path = os.path.join('backend', 'models', 'model.pth')
    torch.save(model.state_dict(), out_path)
    print(f"Saved model to {out_path}")

if __name__ == '__main__':
    # Example: python ml_models/train.py data/small
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('data_dir')
    parser.add_argument('--epochs', type=int, default=1)
    args = parser.parse_args()
    train(args.data_dir, epochs=args.epochs)
