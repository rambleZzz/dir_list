#coding:utf-8
import os

path = r'C:\Users\chanct\Desktop\wordpress'
files = []
dirs = []
datas = {'files':files,'dirs':dirs}
exts = ['.php','.jpg']
def dir_list(path):
    all_files = os.listdir(path)
    for filename in all_files:
        file_path = os.path.join(path,filename)
        if os.path.isdir(file_path):
            dirs.append(file_path)
            dir_list(file_path)
        elif os.path.isfile(file_path):
            for ext in exts:
                if os.path.splitext(file_path)[1] == ext:
                    files.append(file_path)
    return datas

if __name__ == '__main__':
    a = dir_list(path)
    with open('result.txt','w') as f:
        for file in a['files']:
            file_info = file[len(path):]
            print file_info
            f.write(file_info + '\n')
        for dir in a['dirs']:
            dir_info = dir[len(path):]
            print dir_info
            f.write(dir_info + '\n')





