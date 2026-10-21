import random 
import numpy as np
import torch

SEED = 42

random.seed(SEED)   ## python in-built random

np.random.seed(SEED)  ## Numpy random

torch.manual_seed(SEED)  ## pytorch random cpu

if torch.cuda.is_available():  ## if gpu is available
    torch.cuda.manual_seed(SEED)
    torch.cuda.manual_seed_all(SEED)

torch.backends.cudnn.deterministic = True  #CUDA operations को ज्यादा deterministic बनाना
torch.backends.cudnn.benchmark = False

print(random.randint(1, 100))
print(np.random.randint(1, 100))
print(torch.randint(1, 100, (1,)))

# PyTorch DataLoader

from torch.utils.data import DataLoader

generator = torch.Generator().manual_seed(SEED)

train_loader = DataLoader(
    train_dataset,
    batch_size = 32,
    shuffle= True,
    generator= generator
)

import random
import numpy as np
import torch

def set_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False





