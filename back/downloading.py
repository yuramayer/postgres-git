"""Saving DDL files to the local storage"""

import os
import pandas as pd


def save_script(row: pd.Series, schema_path: str, script_type: str):
    """Save downloaded sql DDL script to the local folder"""

    script_name = row.script_name
    script_code = row.script_code

    script_file_path = get_script_path(schema_path, script_type, script_name)

    with open(script_file_path, 'w', encoding='utf-8') as f:
        f.write(script_code)


def get_script_path(schema_path: str, script_type: str,
                    script_name: str) -> str:
    """Get full filepath & name for the new file from database"""

    script_file_name = f'{script_name}.sql'

    candidate = os.path.join(schema_path, script_type, script_file_name)

    counter = 1

    # we save the file without params,
    # but our funcs in the db can be same with different params
    # that's why we should save them as <func.sql>, <func_2.sql> etc
    while os.path.exists(candidate):

        new_name = f'{script_name}_{counter}.sql'
        candidate = os.path.join(schema_path, script_type, new_name)
        counter += 1

    return candidate
