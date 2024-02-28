# EpicMiniProjectBlock3
CS4422 - Data Centric Computing Mini Project

Group 7: 
* Ruan O’Dowd (23381574)
* Jack Casey (23357614)
* Ushen Wijayaratne (23362073)
* Conor Browne (23362308)

## Project Setup 
Using docker:
```
docker-compose up --build
```

Manually:
```
# Install requirements
pip install -r requirements.txt

# Instantiates the schema within the database, and loads sample data
python run_sql_script.py ddl

# Starts the server
python manage.py runserver 0.0.0.0:8000
```

The app will then be accessible at http://localhost:8000