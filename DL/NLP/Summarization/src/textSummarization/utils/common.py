'''
About Utils: 
why utils-- say u r using any function frequently then we write say func-read_yaml 
then we will write func-read_yaml in util folder so as to use it agian and again anywhere needed.

'''



import os
from box.exceptions import BoxValueError      # box exception - read abt it
import yaml
from textSummarization.logging import logger   # our custom logger
from ensure import ensure_annotations
from box import ConfigBox                      
# its awesome- we dont need to put ["key"] for getting the value for that key... we can use d.key only.. & this will give me the value
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
# say we will be creating a folder artifcats -  inside it a folder name data_ingestion: so we will just call this function.


@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories

    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")




@ensure_annotations               
def get_size(path: Path) -> str:
    """get size in KB

    Args:
        path (Path): path of the file

    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"


