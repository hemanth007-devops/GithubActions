# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory
WORKDIR /app

# Copy the requirements.txt file and install any dependencies
COPY ETL-Project/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the ETL script
COPY ETL-Project/etl_script.py .

# Command to run your ETL script
CMD ["python", "etl_script.py"]
