import boto3
import os

def lambda_handler(event, context):
    # TODO implement
    #dynamodb = boto3.resource("dynamodb")
    #table = dynamodb.Table("DoesNotExist")
    #table.put_item(Item=event)
    raise Exception("Really bad thing happens!")
    return {
        "version":"bad"
    }
