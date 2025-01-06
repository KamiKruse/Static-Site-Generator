from textnode import TextNode
import os
import shutil

#Top level function to clean the directory and copy the directory recursively
def clean_and_copy_directory(src, dst):
    if os.path.exists(dst):
        shutil.rmtree(dst)
    copy_directory_recursively(src, dst)

def copy_directory_recursively(src, dst):
    #Base case 1: the source directory does not exist
    if not os.path.exists(src):
        return
   
    os.makedirs(dst, exist_ok=True)

    #Base case 2: the source directory does not exist so the loop will not continue
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            # Base case 3: Found a file, copy and done with this branch
            with open(src_path, 'rb') as fsrc:
                with open(dst_path, 'wb') as fdst:
                    fdst.write(fsrc.read())
        elif os.path.isdir(src_path):
            copy_directory_recursively(src_path, dst_path)


def main():
    clean_and_copy_directory("static", "public")

main()
