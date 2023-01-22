import json
import boto3


def handler(event, context):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("demo-table")

    response = table.scan()
    return {
        "statusCode": 200,
        "body": json.dumps(response["Items"]),
        "headers": {
            'Content-Type': 'application/json',
        }
    }
