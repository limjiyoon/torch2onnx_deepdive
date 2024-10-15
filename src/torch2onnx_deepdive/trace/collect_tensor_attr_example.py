"""Example code that collects tensor attributes of a PyTorch model."""

import torch
import torch.nn as nn


class CustomModel(nn.Module):
    """Custom model with tensor attributes."""

    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, stride=1, padding=1)
        self.fc = nn.Linear(16 * 32 * 32, 10)
        self.some_tensor = torch.randn(5, 5)  # Tensor attribute
        self.submodule = SubModule()

    def forward(self, x: torch.Tensor):
        x = self.conv1(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)


class SubModule(nn.Module):
    """Submodule with tensor attributes."""

    def __init__(self):
        super().__init__()
        self.sub_tensor = torch.randn(3, 3)  # Another Tensor attribute


class CustomTracer:
    """Tracer class that collects tensor attributes."""

    def __init__(self):
        self.tensor_attrs = {}

    def collect_tensor_attrs(self, m: nn.Module, prefix_atoms: list):
        """Recursively collect tensor attributes of a model."""
        for k, v in m.__dict__.items():
            if isinstance(v, torch.Tensor):
                # Save tensor attribute path
                self.tensor_attrs[v] = ".".join(prefix_atoms + [k])
        for k, v in m.named_children():
            # Recursively search child modules
            self.collect_tensor_attrs(v, prefix_atoms + [k])


if __name__ == "__main__":
    model = CustomModel()
    tracer = CustomTracer()
    tracer.collect_tensor_attrs(model, [])
    print(tracer.tensor_attrs)
