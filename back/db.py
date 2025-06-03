"""Creating Engine & queries for the DB"""

from sqlalchemy import create_engine
from dotenv import load_dotenv
from config import DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD

load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def get_views_query(schema: str):
    """Postgres query, get the DDL of the views"""

    return f"""
    select
    c.relname as script_name,
    'CREATE OR REPLACE VIEW ' || quote_ident(n.nspname)
      || '.' || quote_ident(c.relname) || ' AS
    ' || pg_get_viewdef(c.oid, true) as script_code
    from pg_class c
    join pg_namespace n on n.oid = c.relnamespace
    where c.relkind = 'v' and n.nspname = '{schema}'
    ;
    """


def get_funcs_query(schema: str):
    """Postgres query, get the DDL of the funcs"""

    return f"""
    select  p.proname script_name,
    pg_get_functiondef(p.oid) script_code
    from pg_proc p
    join pg_namespace n on n.oid = p.pronamespace
    where n.nspname = '{schema}'
    ;
    """
