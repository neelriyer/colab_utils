import gc
import torch

__all__ = ['free_mem']

def free_mem():
	gc.collect()
	torch.cuda.empty_cache()