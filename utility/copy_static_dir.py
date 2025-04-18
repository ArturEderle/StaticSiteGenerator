import os
import shutil

def copy_contents(src, dst):
    os.mkdir(dst)
    src_contents = os.listdir(src)

    for item in src_contents:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_contents(src_path, dst_path)
