import torch
import torch.nn as nn
import torch.optim as optim

# 1. Define the Neural Network Architecture
class SimpleNet(nn.Module):
    def __init__(self):
        super(SimpleNet, self).__init__()
        # 10 input features -> 16 hidden neurons -> 2 output classes
        self.fc1 = nn.Linear(10, 16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(16, 2)

    def forward(self, x):
        x = self.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# 2. Setup Data, Model, and Training components
model = SimpleNet()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Dummy Data: 5 samples with 10 features each
dummy_inputs = torch.randn(5, 10)
# Dummy Targets: Labels 0 or 1
dummy_targets = torch.tensor([0, 1, 0, 1, 0])

# 3. Simple Training Loop
for epoch in range(5):
    optimizer.zero_grad()           # Reset gradients
    outputs = model(dummy_inputs)   # Forward pass
    loss = criterion(outputs, dummy_targets) # Calculate loss
    loss.backward()                 # Backpropagation
    optimizer.step()                # Update weights
    
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")

# 4. Inference (Making a prediction)
model.eval()
with torch.no_grad():
    prediction = model(dummy_inputs[0].unsqueeze(0))
    predicted_class = torch.argmax(prediction, dim=1)
    print(f"\nPredicted class for first sample: {predicted_class.item()}")