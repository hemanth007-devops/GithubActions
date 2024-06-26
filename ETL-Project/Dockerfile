# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /ETL-Project

# Copy the requirements.txt file and install any dependencies
COPY ETL-Project/requirements.txt ./ETL-Project/requirements.txt
RUN pip install --no-cache-dir -r ETL-Project/requirements.txt

# Copy the ETL script
COPY ETL-Project/etl_script.py ./ETL-Project/etl_script.py

# Command to run your ETL script
CMD ["python", "ETL-Project/etl_script.py"]
