from torch import device
from torch.cuda import current_device, is_available

from config import USE_CUDA

DEVICE = current_device() if is_available() and USE_CUDA else device('cpu')
