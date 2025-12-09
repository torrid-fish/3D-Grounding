# Local Installation
```bash
# Create and activate conda environment
conda create -n 3d_grand_hf python=3.10 -y
conda activate 3d_grand_hf
# Install dependencies
uv pip install -r requirements.txt
# Download model weights and other necessary files
python download.py 
```

# To run:
```
python app.py
```
