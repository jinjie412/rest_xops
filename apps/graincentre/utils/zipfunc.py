import os
import shutil
import zipfile
from os.path import join, getsize, split
import time

def zip_dir(src_dir):
    zip_name = src_dir +'.zip'
    z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)
    for dirpath, dirnames, filenames in os.walk(src_dir):
        fpath = dirpath.replace(src_dir,'')
        fpath = fpath and fpath + os.sep or ''
        for filename in filenames:
            print(filename)
            print('='* 10)
            print(os.path.join(dirpath, filename),fpath+filename)
            z.write(os.path.join(dirpath, filename),fpath+filename)
            print ('==压缩成功==')
    z.close()

def zip_file(file_name, bak_dir):
    try:
        zip_name = file_name +'.zip'
        s_time = time.strftime('%Y.%m.%d_%H.%M.%S',time.localtime(time.time()))
        fpath, name = split(file_name)
        bak_name = s_time +"_"+ name + ".zip"
        bak_name = os.path.join(bak_dir, bak_name)
        # print("bak bak name: ", bak_name)
        z = zipfile.ZipFile(bak_name,'w',zipfile.ZIP_DEFLATED)
        z.write(file_name, name)
        return bak_name
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    b = zip_file("/Users/jin/rest_xops/./db/db/db.sqlite3", "/Users/jin/rest_xops/./db/bak")
    print(b)