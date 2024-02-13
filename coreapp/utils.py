def fetchall_dict(cursor):
    """
    This allows for DB queries to return dictionaries of column : value pairs,
    instead of an opaque array of arrays
    Adapted from https://docs.djangoproject.com/en/5.0/topics/db/sql/
    """
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]