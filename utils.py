"""Path funcs for the project"""

import os
import shutil
import logging
from config import RES_DIR

DIRNAME = f'{RES_DIR}'

if os.path.exists(DIRNAME):
    shutil.rmtree(DIRNAME)

if not os.path.exists(DIRNAME):
    os.mkdir(DIRNAME)


def setup_logger():
    """Info settings for the logger"""

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s - %(message)s"
    )
