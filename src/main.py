from textnode import TextNode
from generate_page import generate_pages_recursive
import os
import shutil

dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"


def clean_and_copy_directory(src, dst):
    print("Deleting public directory...")
    if os.path.exists(dst):
        shutil.rmtree(dst)
    print("Copying static files to public directory...")
    copy_directory_recursively(src, dst)

def copy_directory_recursively(src, dst):
    if not os.path.exists(src):
        return
   
    os.makedirs(dst, exist_ok=True)

   
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            with open(src_path, 'rb') as fsrc:
                with open(dst_path, 'wb') as fdst:
                    fdst.write(fsrc.read())
        elif os.path.isdir(src_path):
            copy_directory_recursively(src_path, dst_path)


def main():
    clean_and_copy_directory(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public)

main()
