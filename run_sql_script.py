import django
from django.db import connection, DatabaseError

import sqlparse

import os
import sys
import glob

def run_sql_script(path):
    with open(path) as f:
        raw_contents = f.read()

    with connection.cursor() as cursor:
        for command in sqlparse.split(raw_contents):
            try:
                cursor.execute(command)
            except DatabaseError as e:
                print (f'Error running command: "{command}": {e}')
                sys.exit(1)

def error_print(msg):
    print ("\033[91m") # Print whatever comes next in red ...
    print (msg)
    print ("\033[0m") # ... then reset to the default text color

if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clubhub.settings')
    django.setup()

    if len(sys.argv) != 2:
        error_print("Error: Make sure you pass in the DDL file or folder! (e.g. python run_sql_script.py ddl)")
        sys.exit(1)
        
    path = sys.argv[1]
    
    if not os.path.exists(path):
        error_print(f"Error: path '{path}' does not exist!")
        
    if os.path.isdir(path):
        for sql_file in sorted(glob.glob(f"{path}/*.sql")):
            run_sql_script(sql_file)
    else:
        run_sql_script(path)
