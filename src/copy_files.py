import os
import shutil
import logging

logger = logging.getLogger(__name__)

def prep_dest(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        os.mkdir(path)
        logger.info(f"Deleted and recreated {path}")
    else:
        os.mkdir(path)
        logger.info(f"Created {path}")

def copy_files(src_path: str, dest_path: str):
    if os.path.exists(src_path) and os.path.exists(dest_path):
        files_to_copy = os.listdir(src_path)

        for item in files_to_copy:
            logger.info(f"Checking {item}")
            path = os.path.join(src_path, item)
            if os.path.isfile(path):
                logger.info(f"{item} is a file. Attempting to copy {path} to {dest_path}")
                shutil.copy(path, dest_path)
            else:
                logger.info(f"{item} is a dir. Extenting dest path and making the dir.")
                dest_path_new = os.path.join(dest_path, item)
                os.mkdir(dest_path_new)
                copy_files(path, dest_path_new)
    else:
        logger.warning(f"Bad path in either {src_path} or {dest_path}")

