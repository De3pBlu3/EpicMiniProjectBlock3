"""
SQLite doesn't allow DB-level triggers.
As such - we need a create and update trigger on every table in our database.
This gets quite tedious to create by hand!

This script creates a SQL file that creates create and update triggers
for every table in our schema.
"""

def generate_trigger_sql(table_name, primary_key):
    return f"""
CREATE TRIGGER {table_name}_created_timestamp AFTER INSERT ON {table_name}
BEGIN
    UPDATE {table_name} SET created = unixepoch('now') WHERE {primary_key} = NEW.{primary_key};
END;

CREATE TRIGGER {table_name}_updated_timestamp AFTER UPDATE ON {table_name}
BEGIN
    UPDATE {table_name} SET updated = unixepoch('now') WHERE {primary_key} = NEW.{primary_key};
END;
"""

def main(table_names):
    generated_sql = "-- Generated automatically by generate_created_updated_triggers.py"
    
    for (table, primary_key) in table_names:
        generated_sql += generate_trigger_sql(table, primary_key)
        
    with open("3_created_updated_triggers.sql", "w") as f:
        f.write(generated_sql)

if __name__ == "__main__":
    main([
        ("users", "id"),
        ("user_applications", "user_id"),
        ("user_username", "user_id"),
        ("user_email", "user_id"),
        ("user_phone", "user_id"),
        ("memberships", "user_id"),
        ("clubs", "id"),
        ("club_applications", "club_id"),
        ("events", "id"),
        ("event_applications", "event_id"),
        ("venues", "id")
    ])