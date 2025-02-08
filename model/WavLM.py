# 
import torch
import torch.nn as nn

from transformers import WavLMConfig, WavLMModel


# WavLM Antispoof model
class WavLMAntispoof(torch.nn.Module):
    def __init__(self, cfg: dict):
        model = self._load_model()
        self.cfg = cfg

    def _load_model(self):
        self.backbone = WavLMModel(WavLMConfig)
        self.header = nn.Linear()
        import pdb
        pdb.set_trace()
        
    def forward():
        
        return 