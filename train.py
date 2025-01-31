import os
import argparse
from utils import utils_model

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

def fetech_model()-> None:
    pass

def parse_argument()-> None:
    args = argparse.ArgumentParser(prog="Audio Deepfake Triner")
    args.add_argument("-c","--config",type=str,default="config/WavLM.yaml")
    args.add_argument("-m","--mode",type=str,default="train")
    return args

if __name__ == "__main__":
    cfg = parse_argument()
    