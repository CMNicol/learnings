def handler(event, context):
    message = "Hello World"
    if params := event.get("queryStringParameters"):
        if name := params.get("name"):
            message = f"Hello {name}"

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "isBase64Encoded": False,
        "body": message,
    }
