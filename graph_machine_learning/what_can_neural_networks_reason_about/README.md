# What can neural networks reason about?
> Neural network structures that align better with the underlying reasoning algorithm generalize better in reasoning tasks.

[paper](https://arxiv.org/abs/1905.13211), [blog post](https://kushajveersingh.github.io/blog/graph_machine_learning/2020/11/07/post-0013.html)

Overview of the files in the directory:
* [src/min_max_mlp_data.py](src/min_max_mlp_data,py): PyTorch dataloader to create dataset for Maximum Value Difference task.
* [src/model_mlp.py](src/model_mlp.py): Create's a MLP for the above datalaoder.
* [notebooks/mlp.ipynb](notebooks/mlp.ipynb): Test MLP on the dataset. It achieves around 8% accuracy.
* [src/min_max_graph_data.py](src/min_max_graph_data.py): Uses pytorch_geometric to construct a 25-node fully connected graph for the Maximum Value Difference task.
* [src/model_gnn.py](src/model_gnn.py): Constructs a GNN for the above dataloader.
* [notebooks/gnn.ipynb](notebooks/gnn.ipynb): Test GNN on the dataset. It achieves around 98.5% accuracy.