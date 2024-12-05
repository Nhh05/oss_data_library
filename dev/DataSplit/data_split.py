import os
import random
from shutil import copy2

def split_image(source_dir, train_dir, test_dir, train_ratio=0.7):
    
    for dir_path in [train_dir, test_dir]:      #train_dir와 test_dir가 가리키는 폴더를 확인한뒤 만약 폴더가 존재한다면 해당폴더와 하위파일을 전부 삭제하고 다시생성
        if os.path.exists(dir_path):
            rmtree(dir_path)
        os.makedirs(dir_path,exist_ok=True)

    all_files = []
    for f in os.listdir(source_dir):    #source_dir 변수가 지정하고 있는 폴더안에 있는 .png 파일 찾아서 모두 all files 리스트에 추가
        if f.endswith('.png'):
            all_files.append(f)
    
    random.shuffle(all_files)       #리스트 안에 있는 .png 파일 전부 무작위로 섞기

    split_index = int(len(all_files) * train_ratio)     #정해둔 train_ratio(비율) 과 .png가 들어있는 리스트의 길이를 곱한 값을 split_index에 저장
    train_files = all_files[:split_index]       #split_index값을 기준으로 그 앞까지는 학습용으로 구분
    test_files = all_files[split_index:]    #split_index값을 기준으로 그 뒤부터는 테스트용으로 구분


    os.makedirs(train_dir, exist_ok=True)       #자신이 속한 디렉토리에 train_dir변수가 지정하고 있는 파일이 없으면 생성
    os.makedirs(test_dir, exist_ok=True)        #자신이 속한 디렉토리에 test_dir변수가 지정하고 있는 파일이 없으면 생성

    for file in train_files:
        copy2(os.path.join(source_dir, file), os.path.join(train_dir, file))   #train_files 에 있던 .png파일과 같은 이름의 원본파일을 train_dir변수가 가리키는 폴더로 복사 

    for file in test_files:
        copy2(os.path.join(source_dir, file), os.path.join(test_dir, file))     #test_files 에 있던 .png파일과 같은 이름의 원본파일을 test_dir변수가 가리키는 폴더로 복사 

# source_dir = "source_files"  
# train_dir = "train_files"    
# test_dir = "test_files"      

# split_image(source_dir, train_dir, test_dir, train_ratio=0.7)
