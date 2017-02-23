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


# move files to separate folder
def get_files(path):
    for d in os.listdir(path):
        filepath = os.path.join(path, d)
        if os.path.isdir(d) and '.' not in d:
            get_files(filepath)
        elif '.html' in d:
            try:
                shutil.move(filepath, './html')
            except Exception as e:
                print(e)


get_files('.')
