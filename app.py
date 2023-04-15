import json
import boto3

client_ses = boto3.client('ses')

def lambda_handler(event, context):
    response = client_ses.send_email(
        Source='anshumanth1997@gmail.com',
        Destination={
            'ToAddresses': [
                'anshumanth1997@gmail.com'
            ]
        },
        Message={
            'Subject': {
                'Data': 'Low Utilization EC2 instances'
            },
            'Body': {
                'Text': {
                    'Data': "An object has been uploaded to your S3 bucket"
                }
            }
        }
    )
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
