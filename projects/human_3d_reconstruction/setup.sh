# install miniconda
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh -b
rm Miniconda3-latest-Linux-x86_64.sh
conda init bash
source ~/.bashrc

# setup environment
conda create -y --name human_3d python=3.7
source ~/miniconda3/etc/profile.d/conda.sh
conda activate human_3d
pip install torch==1.11.0+cu113 torchvision==0.12.0+cu113 --extra-index-url https://download.pytorch.org/whl/cu113
python3 -m pip install matplotlib==3.4.3 scipy==1.7.3 lpips==0.1.4 facenet-pytorch==2.5.2 ninja==1.10.2.3 scikit-image==0.18.3 trimesh==3.14.0 PyOpenGL==3.1.6 pycocotools==2.0.4
conda install -y -c conda-forge opencv=4.5.5

# setup insetgan repo
# git clone https://github.com/afruehstueck/insetGAN.git insetgan
# rm -rf insetgan/.git insetgan/.gitignore
# git clone https://github.com/NVlabs/stylegan2-ada-pytorch.git temp
# cp -r temp/dnnlib insetgan/
# cp -r temp/torch_utils insetgan/
# rm -rf temp
# x=`printf "import warnings\nwarnings.filterwarnings('ignore')\n"; cat insetgan/run_insetgan.py`
# echo "$x" > insetgan/run_insetgan.py
mkdir insetgan/networks
wget -P insetgan/networks https://github.com/KushajveerSingh/human_3d_reconstruction/releases/download/v0.0.1/DeepFashion_1024x768.pkl
wget -P insetgan/networks https://github.com/KushajveerSingh/human_3d_reconstruction/releases/download/v0.0.1/ffhq.pkl
cd insetgan
python run_insetgan.py
cd ..
rm -rf results

# setup pifudh repo
# git clone https://github.com/facebookresearch/pifuhd.git
# rm -rf pifuhd/.git pifuhd/.gitignore
# chmod u+x pifuhd/scripts/demo.sh
mkdir -p pifuhd/checkpoints
wget -P pifuhd/checkpoints https://dl.fbaipublicfiles.com/pifuhd/checkpoints/pifuhd.pt

# setup pose estimation repo
# cd pifuhd
# git clone https://github.com/Daniil-Osokin/lightweight-human-pose-estimation.pytorch.git pose
# cd pose
# rm -rf .git .gitignore
# cd ../../
wget -P pifuhd/pose https://download.01.org/opencv/openvino_training_extensions/models/human_pose_estimation/checkpoint_iter_370000.pth