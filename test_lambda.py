import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(os.environ['USER_TABLE'])
    return {
        "version":"second version"
    }
