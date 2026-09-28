import numpy as np
import pandas as pd
from tqdm import tqdm
from dotenv import load_dotenv
from loguru import logger

print("=" * 50)
print("Ank-One Library Test")
print("=" * 50)

print("NumPy Version :", np.__version__)
print("Pandas Version:", pd.__version__)

load_dotenv()

logger.success("All libraries loaded successfully!")

for i in tqdm(range(5), desc="Testing"):
    pass

print("\nEverything is working correctly!")