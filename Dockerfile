# Use an official Python runtime as a parent image
FROM python:3.11.5

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /clubhub

# Install dependencies
COPY requirements.txt /clubhub/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . $SRCDIR

# Create the directory for the SQLite database, set the correct permissions, and run the script
RUN mkdir -p /var/lib/sqlite && \
    chown -R www-data:www-data /var/lib/sqlite && \
    python run_sql_script.py ddl

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]