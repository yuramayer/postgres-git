"""The app that saves DDL's to the local storage for the git"""

import logging
import os
import pandas as pd
from config import SCHEMAS, RES_DIR
from utils import setup_logger
from back.db import engine, get_views_query, get_funcs_query
from back.downloading import save_script


def main():
    """The main app function"""

    setup_logger()

    logger = logging.getLogger(__name__)

    for schema in SCHEMAS:

        logger.info('schema %s : functions', schema)

        schema_path = os.path.join(RES_DIR, schema)
        os.makedirs(os.path.join(schema_path, 'functions'), exist_ok=True)
        os.makedirs(os.path.join(schema_path, 'views'), exist_ok=True)

        with engine.connect() as conn:
            funcs_query = get_funcs_query(schema)
            funcs_df = pd.read_sql(funcs_query, conn)

        funcs_df.apply(save_script, args=(schema_path, 'functions'), axis=1)

        logger.info('schema %s : views', schema)

        with engine.connect() as conn:
            views_query = get_views_query(schema)
            views_df = pd.read_sql(views_query, conn)

        views_df.apply(save_script, args=(schema_path, 'views'), axis=1)


if __name__ == '__main__':
    main()
