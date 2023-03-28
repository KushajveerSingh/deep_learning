cd insetgan
python run_insetgan.py

cd ../pifuhd/pose
python pose.py

cd ../../pifuhd
python -m apps.simple_test
cd ..