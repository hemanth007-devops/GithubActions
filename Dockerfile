# Use the AWS Lambda Python runtime as the base image
FROM public.ecr.aws/lambda/python:3.8

# Set working directory to root
WORKDIR /

# Install AWS SDK (boto3) for AWS Glue
RUN pip install boto3

# Copy Lambda handler script
COPY lambda_handler.py .

# Command to run Lambda handler function
CMD ["lambda_handler.lambda_handler"]
