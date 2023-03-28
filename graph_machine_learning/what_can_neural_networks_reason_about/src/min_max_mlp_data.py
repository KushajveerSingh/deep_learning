import numpy as np
import torch
from torch.utils.data import Dataset, DataLoader
from pytorch_lightning import LightningDataModule


class MinMaxDiffDataset(Dataset):
    """
    Dataset for Maximum value difference problem as presented in the paper
    https://arxiv.org/abs/1905.13211.
    """
    def __init__(self, num_samples: int):
        # 25 = num objects to sample
        # 8 = size of location vector
        # 1 = size of value vector
        # 1 = size of color vector
        self.data = torch.empty(num_samples, 25*(8+1+1), dtype=torch.float32)
        self.y = torch.empty(num_samples, dtype=torch.int64)

        for i in range(num_samples):
            # These defaults are same as given in the paper
            location = np.random.uniform(0, 20, size=(25, 8))
            value = np.random.randint(100, size=(25, 1))
            color = np.random.randint(1, 6, size=(25, 1))

            min_val = np.min(value)
            max_val = np.max(value)

            t = np.concatenate((location, value, color), axis=1).flatten()

            self.data[i] = torch.tensor(t, dtype=torch.float32)
            self.y[i] = torch.tensor(int(max_val - min_val), dtype=torch.int64)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.y[idx]


class MinMaxDiffModule(LightningDataModule):
    def __init__(self, train_size=50000, val_size=5000):
        super().__init__()
        self.train_size = train_size
        self.val_size = val_size

    def setup(self, stage=None):
        if stage == "fit" or stage is None:
            self.train_dataset = MinMaxDiffDataset(self.train_size)
            self.val_dataset = MinMaxDiffDataset(self.val_size)

    def train_dataloader(self):
        return DataLoader(self.train_dataset,
                          batch_size=128,
                          shuffle=True,
                          drop_last=True)

    def val_dataloader(self):
        return DataLoader(self.val_dataset,
                          batch_size=1024)
