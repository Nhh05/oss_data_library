import os
import random
from shutil import copy2

def split_image(source_dir, train_dir, test_dir, train_ratio=0.7):
    
    for dir_path in [train_dir, test_dir]:
        if os.path.exists(dir_path):
            rmtree(dir_path)
        os.makedirs(dir_path,exist_ok=True)

    all_files = []
    for f in os.listdir(source_dir):
        if f.endswith('.png'):
            all_files.append(f)
    
    random.shuffle(all_files)

    split_index = int(len(all_files) * train_ratio)
    train_files = all_files[:split_index]
    test_files = all_files[split_index:]

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for file in train_files:
        copy2(os.path.join(source_dir, file), os.path.join(train_dir, file))

    for file in test_files:
        copy2(os.path.join(source_dir, file), os.path.join(test_dir, file))

source_dir = "source_files"  
train_dir = "train_files"    
test_dir = "test_files"      

split_image(source_dir, train_dir, test_dir, train_ratio=0.7)
