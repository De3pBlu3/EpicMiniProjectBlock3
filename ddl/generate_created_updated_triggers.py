"""
SQLite doesn't allow DB-level triggers.
As such - we need a create and update trigger on every table in our database.
This gets quite tedious to create by hand!

This script creates a SQL file that creates create and update triggers
for every table in our schema.
"""

def generate_trigger_sql(table_name):
    return f"""
CREATE TRIGGER {table_name}_created_timestamp AFTER INSERT ON {table_name}
BEGIN
    UPDATE {table_name} SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER {table_name}_updated_timestamp AFTER UPDATE ON {table_name}
BEGIN
    UPDATE {table_name} SET updated = unixepoch('now') WHERE id = NEW.id;
END;
"""

def main(table_names):
    generated_sql = "-- Generated automatically by generate_created_updated_triggers.py"
    
    for table in table_names:
        generated_sql += generate_trigger_sql(table)
        
    with open("3_created_updated_triggers.sql", "w") as f:
        f.write(generated_sql)

if __name__ == "__main__":
    main([
        "users",
        "user_applications",
        "user_usernames",
        "user_emails",
        "user_phones",
        "memberships",
        "clubs",
        "club_applications",
        "events",
        "event_applications",
        "venues"
    ])