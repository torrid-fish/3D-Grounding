import os
import sys

os.environ["HF_HUB_ENABLE_HF_TRANSFER"] = "1"
from huggingface_hub import hf_hub_download, snapshot_download

REPO_ID = "TorridFish/3D-Grounding-Model-and-Data"
ALLOW_PATTERNS = ["checkpoints/*", "data/*"]


try:
    snapshot_download(
        repo_id=REPO_ID,
        allow_patterns=ALLOW_PATTERNS,
        local_dir=".",
        local_dir_use_symlinks=False,
        repo_type="model",
    )
    print("Download completed successfully.")
except Exception as e:
    print(f"An error occurred during download: {e}")
    sys.exit(1)
