import os
import shutil
import sys
from utility.copy_static_dir import copy_contents
from src.gencontent import generate_pages_recursive

base_dir = os.path.dirname(os.path.abspath(__file__))
dir_path_static = os.path.abspath(os.path.join(base_dir, '..', 'static'))
dir_path_public = os.path.abspath(os.path.join(base_dir, '..', 'docs'))
dir_path_content = os.path.abspath(os.path.join(base_dir, '..', 'content'))
template_path = os.path.abspath(os.path.join(base_dir, '..', 'docs/template.html'))


def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if not os.path.exists(dir_path_static):
        raise Exception(f"Source {dir_path_static} doesn't exists")

    if os.path.exists(dir_path_public):
        print(f"Destination {dir_path_public} already exists - REMOVING")
        shutil.rmtree(dir_path_public)

    copy_contents(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

if __name__ == "__main__":
    main()



