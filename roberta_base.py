# roberta_base_download.py
import os, shutil
from modelscope import snapshot_download

# 脚本同级目录；在交互环境则为当前工作目录
try:
    root_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    root_dir = os.getcwd()

target_dir = os.path.join(root_dir, 'roberta-base')   # 目标目录（脚本同级）
cache_dir  = os.path.join(root_dir, '.ms_cache')      # 可选：本地缓存目录
os.makedirs(target_dir, exist_ok=True)
os.makedirs(cache_dir, exist_ok=True)

model_id = 'AI-ModelScope/roberta-base'

# 旧版 modelscope 不支持 local_dir_use_symlinks——不用它
try:
    model_dir = snapshot_download(model_id, local_dir=target_dir, cache_dir=cache_dir)
except TypeError:
    # 极旧版本可能连 local_dir 都不生效：退回只用 cache_dir，后面手动拷贝
    model_dir = snapshot_download(model_id, cache_dir=cache_dir)

# 如果实际下载目录不是 target_dir，则把内容拷过去（避免仅留在缓存）
if os.path.abspath(model_dir) != os.path.abspath(target_dir):
    for name in os.listdir(model_dir):
        src = os.path.join(model_dir, name)
        dst = os.path.join(target_dir, name)
        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

print('模型已下载到:', target_dir)