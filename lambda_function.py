import json

def lambda_handler(event, context):
    
    response = {
        "statusCode": 302,
        "statusDescription": "Found",
        "isBase64Encoded": False,
        "headers": {
            "Location": "https://www.aithertechnology.com/blog/"
        }
    }
        
    return response