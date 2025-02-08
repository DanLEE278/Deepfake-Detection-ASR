import argparse
import yaml

def parse_args()-> argparse.Namespace:
    args = argparse.ArgumentParser(prog="Audio Deepfake Triner")
    args.add_argument("-c","--config",type=str,default="config/WavLM.yaml")
    args.add_argument("-m","--mode",type=str,default="train")
    return args

def read_yaml(fpath: str)-> dict:
    with open(fpath, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)