import django
from django.db import connection, OperationalError, ProgrammingError

import sqlparse

import os
import sys

def run_sql_script(path):
    with open(path) as f:
        raw_contents = f.read()

    with connection.cursor() as cursor:
        for command in sqlparse.split(raw_contents):
            try:
                cursor.execute(command)
            except (OperationalError, ProgrammingError) as e:
                print (f'Error running command: "{command}": {e}')
                break
            
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clubhub.settings')
    django.setup()
    try:
        run_sql_script(sys.argv[1])
    except IndexError:
        print("\033[91m \n Error: Make sure you pass in the DDL file! (e.g. python run_sql_script.py ddl/create_tables.sql)")

