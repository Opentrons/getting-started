import os
import shutil


os.system("find . -name '*.html' | xargs rm -rf")
os.system("find . -name '.ipynb_checkpoints' | xargs rm -rf")
os.system(
    "find . -name '*.ipynb' | xargs jupyter nbconvert --to html --execute --allow-errors")
os.system("find . -name 'containers' | xargs rm -rf")
os.system("find . -name 'calibrations' | xargs rm -rf")
os.system("find . -name 'smoothie' | xargs rm -rf")
os.system("find . -name 'logs' | xargs rm -rf")
os.system("find . -name 'logs' | xargs rm -rf")


file_path = os.path.dirname(os.path.abspath(__file__))
css_filepath = os.path.join(file_path, 'css/custom.css')


# move files to separate folder
def get_files(path):
    for d in os.listdir(path):
        this_path = os.path.join(path, d)
        if os.path.isdir(this_path) and '.' not in this_path:
            get_files(this_path)
        elif '.html' in d:
            try:
                shutil.copy(this_path, os.path.join(path, 'index.html'))
                os.remove(this_path)
                shutil.copy(css_filepath, path)
            except Exception as e:
                print(e)


get_files(file_path)
