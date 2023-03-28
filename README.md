# Deep Learning
> Collection of my work related to deep learning in a single place.

[https://kushajveersingh.github.io/blog/](https://kushajveersingh.github.io/blog/)

## Repository Structure

1. [graph_machine_learning](graph_machine_learning)

    1. [what_can_neural_networks_reason_about](graph_machine_learning/what_can_neural_networks_reason_about) - Implementation of paper [What can Neural Networks Reason About](https://arxiv.org/abs/1905.13211). Check my [blog post](https://kushajveersingh.github.io/blog/graph_machine_learning/2020/11/07/post-0013.html) for the paper summary. Results from one of the experiments presented in the paper are reproduced. [twitter-card](https://twitter.com/Kkushaj/status/1325445905554706434)

2. [projects](projects)

    1. [Semi-supervised parking lot detection](https://github.com/KushajveerSingh/Unsupervised-Parking-Lot-Detection) -> My submission for Techgig Code Gladiators 2019 AI theme competition that won 1st place at the final.
    2. [Waste Seggregation using trashnet](projects/Waste_Seggregation_using_trashnet) -> Contains the code to train models for trashnet and then export them using ONNX. It was part of a bigger project where we ran these models on Rasberry Pi, which controlled wooden planks to classify the waste into different categories (code for rasberry pi not included here).
    3. [Human 3D Reconstruction](projects/human_3d_reconstruction) -> Uses Insetgan and Pifuhd models to generate 3D full body images of people.

3. [paper_implementations](paper_implementations)

    1. [Photorealistic Style Transfer](https://github.com/KushajveerSingh/Photorealistic-Style-Transfer) - Implementation of [**High Resolution Network for Photorealistic Style Transfer**](https://arxiv.org/abs/1904.11617) 
    2. [SPADE-PyTorch](https://github.com/KushajveerSingh/SPADE-PyTorch) - Implementation of [**Semantic Image Synthesis with Spatially-Adaptive Normalization (SPADE)**](https://arxiv.org/abs/1903.07291)
    3. [Weight Standardization](paper_implementations/weight_standardization) - Implementation of [**Weight Standardization**](https://arxiv.org/abs/1903.10520). Tested using cyclic learning.
    4. [Training AlexNet with tips and checks on how to train CNNs](paper_implementations/Training%20AlexNet%20with%20tips%20and%20checks%20on%20how%20to%20train%20CNNs) - A PyTorch tutorial on how to create an image classifier.
    5. [Study of Mish activation function in transfer learning with code and discussion](paper_implementations/Study%20of%20Mish%20activation%20function%20in%20transfer%20learning%20with%20code%20and%20discussion) - Implementation of [**Mish: A Self Regularized Non-Monotonic Neural Activation Function**](https://arxiv.org/abs/1908.08681).
    6. [Number of bins of a Histogram](paper_implementations/Number%20of%20bins%20of%20a%20Histogram) - Notebook discussing three techniques of choosing the bin size in histograms.
    7. [Multi Sample Dropout](paper_implementations/Multi%20Sample%20Dropout) - Implementation of [**Multi-Sample Dropout for Accelerated Training and Better Generalization**](https://arxiv.org/abs/1905.09788).
    8. [Data Augmentation in Computer Vision](paper_implementations/Data%20Augmentation%20in%20Computer%20Vision) - Notebook implementing single image data augmentation techniques using just Python.
    9.  [How to deal with outlier](paper_implementations/How%20to%20deal%20with%20outliers) - Notebook discussing ways to deal with outliers.
    10. [Leslie N. Smith papers notebook](paper_implementations/Leslie%20N.%20Smith%20papers%20notebook) - Jupyter notebook discussing cyclic learning and ways by which we can choose hyperparameter values by looking at valid loss graph.
        
4. [notes](notes) - My notes when learning some things.

   * [Cython](notes/cython.ipynb)
   * [dask](notes/dask.ipynb)
   * [matplotlib](notes/matplotlib.ipynb)
   * [PIL](notes/PIL.ipynb)
   * [seaborn](notes/seaborn.ipynb)
   * [vim](notes/vim.txt)
   * [xarray](notes/xarray.ipynb)
   * [Python](notes/Python) - Data model + James Powell talks

5. [random](random) - Random scripts and os setup instructions.
   
    1. [os_setup_instructions](random/os_setup_instructions) - My setup guide for Windows 10 and Ubuntu 20.04 (needs to be updated a bit).
    2. [cifar10_data_script.py](random/cifar10_data_script.py) - To convert CIFAR10 data to numpy array
    3. [save_torchvision_models_to_disk](random/save_torchvision_models_to_disk.ipynb) -> a quick script to download all pytorch models
    4. [unscramble_android_game](random/unscramble_android_game) -> Python script to solve the unscramble android game. Complexity is exponential to generate all the substrings, and a dictionary is used to check for valid words.
    5. [download_conference_papers](random/dowload_conference_papers) -> Python scripts to download conference papers as PDFs (like CVPR, ICLR, ECCV) with utility functions what can be used to download papers from any conference.
    6. [dash_cdc_jhu_visualization](random/dash_cdc_jhu_visualization) -> Python program to download CDC and JHU covid data, and then visualize the discrepencies between the two sources of data using Dash.