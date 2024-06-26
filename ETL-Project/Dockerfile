# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /ETL-project

# Copy the requirements.txt file and install any dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ETL script
COPY etl_script.py ./etl_script.py

# Command to run your ETL script
CMD ["python", "etl_script.py"]
