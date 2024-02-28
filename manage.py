#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clubhub.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # if runserver is command line argument:
    # if 'runserver' in sys.argv:
    #     # run the sql script
    #     os.system('python run_sql_script.py ddl')
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
