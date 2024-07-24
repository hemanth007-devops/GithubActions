import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    workflow_name = 'your_glue_workflow_name'  # Replace with your actual Glue workflow name

    try:
        response = glue.start_workflow_run(Name=workflow_name)
        workflow_run_id = response['RunId']
        print(f"Started Glue workflow run with ID: {workflow_run_id}")
        return {
            'statusCode': 200,
            'body': f"Started Glue workflow run with ID: {workflow_run_id}"
        }
    except Exception as e:
        print(f"Error starting Glue workflow: {str(e)}")
        return {
            'statusCode': 500,
            'body': f"Error starting Glue workflow: {str(e)}"
        }
