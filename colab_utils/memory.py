import gc
import torch

def free_mem():
	gc.collect()
	torch.cuda.empty_cache()