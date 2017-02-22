import os


os.system("find . -name '.ipynb_checkpoints' | xargs rm -rf")
os.system(
    "find . -name '*.ipynb' | xargs jupyter nbconvert --to html --execute --allow-errors")
os.system("find . -name 'containers' | xargs rm -rf")
os.system("find . -name 'calibrations' | xargs rm -rf")
os.system("find . -name 'smoothie' | xargs rm -rf")
os.system("find . -name 'logs' | xargs rm -rf")
os.system("find . -name 'logs' | xargs rm -rf")

# move files to separate folder

# parse .html files and modify CSS for Cells' stdout

print('\n\ndone!!')
