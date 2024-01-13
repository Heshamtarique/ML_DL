import os
from pathlib import Path
import logging

logging.basicConfig(level= logging.INFO, format='[%(asctime)s]: %(message)s: ')

project_name = "textSummarization"

list_of_files = [
    "github.com/workflows/.gitkeep/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",    
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configration.py",
    f"src/{project_name}/pipeline/__init__.py.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py"
    "config/config.yaml",
    "parmas.yaml",
    "app.py",
    "main.py",
    "README.md",
    "LICENSE",
    "requirements.txt",
    "Dockerfile",
    "setup.py",
    "exp/trials.ipynb",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True) 
        logging.info(f"creating directory: {filedir} for the file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:            # NOTE: checking if the file size is zero then creating a new directory other wise the Previous code will be overwrriten by blank file
        with open(filepath, 'w') as f:
            pass
            logging.info(f"creating empty file: {filepath}")        
    else:
        logging.info(f"file already exists: {filepath}")
        
        
