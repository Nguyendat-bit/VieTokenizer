import gdown
import os
import shutil
import pickle as pkl 
import tensorflow as tf 
from vietokenizer.constant import (
    model_url, 
    vocab_url, 
    vocab_save, 
    model_save 
)

def handler(func, path, exc_info):
    print("Inside handler")
    print(exc_info)


def ensure_dir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        return False 
    return True
        
def download_model():
    if not ensure_dir(model_save): 
        print('=' * 10 + ' Install Pretrained ' + '=' * 10)
        gdown.download_folder(model_url, output= model_save)

def download_vocab():
    if not ensure_dir(vocab_save): 
        print('=' * 10 + ' Install Vocab ' + '=' * 10)
        gdown.download_folder(vocab_url, output= vocab_save)

def download():
    download_model()
    download_vocab()

def clear_cache_model():
    shutil.rmtree(model_save, onerror= handler)

def clear_cache_vocab():
    shutil.rmtree(vocab_save, onerror= handler)

def clear_cache():
    clear_cache_model()
    clear_cache_vocab()



