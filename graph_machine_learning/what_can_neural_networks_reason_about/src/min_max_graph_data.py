import torch
from torch_geometric.data import Data, InMemoryDataset, DataLoader
from pytorch_lightning import LightningDataModule
from min_max_mlp_data import MinMaxDiffDataset


class MinMaxGraphDataset(InMemoryDataset):
    def __init__(self, num_samples: int):
        """
        Dataset for Maximum value difference problem as presented in the paper
        https://arxiv.org/abs/1905.13211.
        """
        super().__init__()
        dataset = MinMaxDiffDataset(num_samples)
        raw_x = dataset.data.view(num_samples, 25, 10)
        raw_y = dataset.y

        # fully connected graph
        # num_nodes = 25
        edges = []
        for i in range(25):
            for j in range(25):
                if i == j:
                    continue
                else:
                    edges.append([i, j])
        edge_index = torch.tensor(edges, dtype=torch.int64).t().contiguous()

        self.num_samples = num_samples
        self.data = []
        for i in range(num_samples):
            x = raw_x[i].clone().contiguous()
            y = raw_y[i].clone()
            self.data.append(Data(x=x, edge_index=edge_index, y=y))

    def __len__(self):
        return self.num_samples

    def __getitem__(self, idx):
        return self.data[idx]


class MinMaxGraphModule(LightningDataModule):
    def __init__(self, train_size=50000, val_size=5000):
        super().__init__()
        self.train_size = train_size
        self.val_size = val_size

    def setup(self, stage=None):
        if stage == "fit" or stage is None:
            self.train_dataset = MinMaxGraphDataset(self.train_size)
            self.val_dataset = MinMaxGraphDataset(self.val_size)

    def train_dataloader(self):
        return DataLoader(self.train_dataset,
                          batch_size=128,
                          shuffle=True,
                          drop_last=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset, batch_size=512)
