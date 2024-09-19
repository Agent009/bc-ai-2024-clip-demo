import os

import torch
from dotenv import load_dotenv, find_dotenv

# ---------- Load environment variables
load_dotenv(find_dotenv())
CLIP_SERVER_ADDRESS = os.getenv("CLIP_SERVER_ADDRESS")


def get_data_path():
    return "./data/"


def get_clip_server_address():
    return CLIP_SERVER_ADDRESS


def check_cuda():
    """
    This function checks the availability and details of CUDA and GPU for PyTorch.

    It prints the following information:
    1. The CUDA version that PyTorch is using.
    2. Whether a GPU is available for PyTorch.
    3. The name of the GPU if available, otherwise, it prints "No GPU detected".

    Parameters:
    None

    Returns:
    None
    """
    print(f"CUDA version that PyTorch is using: {torch.version.cuda}")
    print(f"GPU is available for PyTorch? {torch.cuda.is_available()}")
    print("GPU if available: " + torch.cuda.get_device_name(0) if torch.cuda.is_available() else "No GPU detected")
