import django
from django.db import connection, OperationalError

import os
import sys

def run_sql_script(path):
    with open(path) as f:
        raw_contents = f.read()
        
    sql_commands = raw_contents.replace("\n", "").split(";")

    with connection.cursor() as cursor:
        for command in sql_commands:
            if command.strip() == "":
                continue
            
            try:
                cursor.execute(command)
            except OperationalError as e:
                print (f'Error running command: "{command}": {e}')
                break
            
if __name__ == "__main__":
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clubhub.settings')
    django.setup()
    run_sql_script(sys.argv[1])