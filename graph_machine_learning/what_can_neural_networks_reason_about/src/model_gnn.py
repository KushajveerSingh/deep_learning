import torch
import torch.nn as nn
import torch_geometric.nn as pyg_nn
from pytorch_lightning import LightningModule
from pytorch_lightning.metrics import Accuracy


class GNN_Layer(pyg_nn.MessagePassing):
    def __init__(self, in_features: int, out_features: int,
                 hidden_mlp_dim: int = 256,
                 aggr='add', num_mlp_layers: int = 3, **kwargs):
        super().__init__(aggr, **kwargs)

        layers = [
            nn.Linear(in_features*2, hidden_mlp_dim),
            nn.ReLU()
        ]
        for _ in range(num_mlp_layers-2):
            layers.append(nn.Linear(hidden_mlp_dim, hidden_mlp_dim))
            layers.append(nn.ReLU())
        layers.append(nn.Linear(hidden_mlp_dim, out_features))

        self.mlp = nn.Sequential(*layers)

    def forward(self, x, edge_index):
        return self.propagate(edge_index, x=x)

    def message(self, x_i, x_j):
        x = torch.cat((x_i, x_j), dim=-1)
        return self.mlp(x)


class GNN_Model(nn.Module):
    def __init__(self, in_features: int = 10, hidden_dim: int = 256,
                 num_layers: int = 4, num_classes: int = 101, **kwargs):
        super().__init__()
        self.layers = nn.ModuleList()
        self.layers.append(GNN_Layer(in_features, hidden_dim, **kwargs))
        for _ in range(num_layers-1):
            self.layers.append(GNN_Layer(hidden_dim, hidden_dim, **kwargs))

        self.linear = nn.Linear(hidden_dim, num_classes)

    def forward(self, x, edge_index, batch):
        for i in range(len(self.layers)-1):
            x = self.layers[i](x, edge_index)
            x = x.relu()
        x = self.layers[-1](x, edge_index)
        x = pyg_nn.global_mean_pool(x, batch)
        # x = nn.functional.dropout(x, p=0.5, training=self.training)
        x = self.linear(x)
        return x


class GNN_Module(LightningModule):
    def __init__(self, in_features: int = 10, hidden_dim: int = 256,
                 num_layers: int = 4, num_classes: int = 101, **kwargs):
        super().__init__()
        self.model = GNN_Model(in_features, hidden_dim, num_layers,
                               num_classes, **kwargs)
        self.loss = nn.CrossEntropyLoss()
        self.val_accuracy = Accuracy()

    def forward(self, x, edge_index, batch):
        return self.model(x, edge_index, batch)

    def training_step(self, batch, batch_idx):
        out = self(batch.x, batch.edge_index, batch.batch)
        loss = self.loss(out, batch.y)
        self.log('train_loss', loss, on_step=False, on_epoch=True)
        return loss

    def validation_step(self, batch, batch_idx):
        out = self(batch.x, batch.edge_index, batch.batch)
        loss = self.loss(out, batch.y)
        acc = self.val_accuracy(out, batch.y)

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
