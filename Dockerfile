FROM python:3.10-alpine

COPY . .
RUN pip install -r requirements.txt
RUN python run_sql_script.py ddl

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000