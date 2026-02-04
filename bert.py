# roberta_base_download.py
import os, shutil
from modelscope import snapshot_download


try:
    root_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    root_dir = os.getcwd()

target_dir = os.path.join(root_dir, 'bert-base-cased')   
cache_dir  = os.path.join(root_dir, '.ms_cache')      
os.makedirs(target_dir, exist_ok=True)
os.makedirs(cache_dir, exist_ok=True)

model_id = 'AI-ModelScope/bert-base-cased'


try:
    model_dir = snapshot_download(model_id, local_dir=target_dir, cache_dir=cache_dir)
except TypeError:
    
    model_dir = snapshot_download(model_id, cache_dir=cache_dir)


if os.path.abspath(model_dir) != os.path.abspath(target_dir):
    for name in os.listdir(model_dir):
        src = os.path.join(model_dir, name)
        dst = os.path.join(target_dir, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

print('The model has been downloaded to:', target_dir)
