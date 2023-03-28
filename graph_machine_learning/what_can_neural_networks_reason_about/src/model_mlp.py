import torch
import torch.nn as nn
from pytorch_lightning import LightningModule
from pytorch_lightning.metrics import Accuracy


def lin_relu(in_features, out_features):
    return nn.Sequential(
        nn.Linear(in_features, out_features),
        nn.ReLU(inplace=True),
    )


class MLP(nn.Module):
    def __init__(self, input_dim=25*(8+1+1),
                 hidden_dim=256, num_layers=6,
                 num_classes=101):
        super().__init__()
        self.layers = nn.ModuleList([lin_relu(input_dim, hidden_dim)])
        for _ in range(num_layers-2):
            self.layers.append(lin_relu(hidden_dim, hidden_dim))
        self.layers.append(nn.Linear(hidden_dim, num_classes))

    def forward(self, x):
        for i in range(len(self.layers)):
            x = self.layers[i](x)
        return x


class MLPModule(LightningModule):
    def __init__(self, input_dim=25*(8+1+1),
                 hidden_dim=256,
                 num_layers=6,
                 num_classes=101):
        super().__init__()
        self.save_hyperparameters()
        self.model = MLP(input_dim, hidden_dim, num_layers, num_classes)
        self.loss = nn.CrossEntropyLoss()
        self.val_accuracy = Accuracy()

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        out = self(x)
        loss = self.loss(out, y)
        self.log('train_loss', loss, on_step=False, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        out = self(x)

        loss = self.loss(out, y)
        acc = self.val_accuracy(out, y)
        self.log('val_loss', loss, prog_bar=True)
        self.log('acc', acc, prog_bar=True)

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.model.parameters(), lr=1e-3)
        lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer,
                                                       step_size=50,
                                                       gamma=0.5)
        return {
            'optimizer': optimizer,
            'lr_scheduler': lr_scheduler,
        }
