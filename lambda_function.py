import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    job_name = 'your_glue_job_name'  # Replace with your actual Glue job name

    try:
        response = glue.start_job_run(JobName=job_name)
        job_run_id = response['JobRunId']
        print(f"Started Glue job run with ID: {job_run_id}")
        return {
            'statusCode': 200,
            'body': f"Started Glue job run with ID: {job_run_id}"
        }
    except Exception as e:
        print(f"Error starting Glue job: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error starting Glue job: {str(e)}"
        }
