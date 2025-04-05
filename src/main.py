import os.path

from textnode import TextNode
import os
import shutil

def copy_contents(src, dst):
    if not os.path.exists(src):
        raise Exception(f"Source {src} doesn't exists")

    if os.path.exists(dst):
        print(f"Destination {dst} already exists - REMOVING")
        shutil.rmtree(dst)
    os.mkdir(dst)
    src_contents = os.listdir(src)

    for item in src_contents:
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
        else:
            copy_contents(src_path, dst_path)

def main():
    print(copy_contents('../static', '../public'))

if __name__ == "__main__":
    main()



