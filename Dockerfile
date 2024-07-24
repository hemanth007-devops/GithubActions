# Use the AWS Lambda Python runtime as the base image
FROM public.ecr.aws/lambda/python:3.8

# Set working directory to /var/task
WORKDIR /var/task

# Copy requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Lambda handler script
COPY lambda_function.py .

# Command to run Lambda handler function
CMD ["lambda_function.lambda_handler"]
