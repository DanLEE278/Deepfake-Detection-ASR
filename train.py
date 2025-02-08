import os
import argparse
from model import WavLMAntispoof
from util import read_yaml

'''
Main Features:
    - This Git repository has been created to easily yet effectively train Audio-based deepfake classifier
    - Python Library has been minimize for easy environmetal setting

V1.0.0 (2025.01.30)
    - training utils update
    - 
    
date: 2025.01.30
'''

def train()-> None:
    pass

def fetech_model(config: dict):
    model = WavLMAntispoof(config)
    return model

def parse_argument()-> None:
    args = argparse.ArgumentParser(prog="Audio Deepfake Triner")
    args.add_argument("-c","--config",type=str,default="config/WavLM.yaml")
    args.add_argument("-m","--mode",type=str,default="train")
    return args.parse_args()

if __name__ == "__main__":
    args = parse_argument()
    config = read_yaml(args.config)
    
    fetech_model(config)
    