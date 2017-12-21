import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("DoesNotExist")
    return {
        "version":"second version"
    }
