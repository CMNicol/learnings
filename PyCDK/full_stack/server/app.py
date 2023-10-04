from flask import Flask, request
from flask_cors import CORS
import boto3
from uuid import uuid4
import os

PORT = os.environ.get("PORT", 80)


app = Flask("CraigsApp")
CORS(app)


@app.route("/healthcheck")
def healthcheck():
    return "OK"


@app.post("/")
def add():
    request_todo = request.get_json()["todo"]
    name = request_todo["name"]
    description = request_todo["description"]
    completed = request_todo["completed"]

    todo = {
        "sort_key": str(uuid4()),
        "partition_table": "todo",
        "name": name,
        "description": description,
        "completed": str(completed,)
    }

    dynamodb = boto3.client("dynamodb")
    dynamodb.put_item(
        TableName="main_table",
        Item={key: {"S": value} for key, value in todo.items()},
    )

    return todo


@app.get("/")
def get_all():
    dynamodb = boto3.client("dynamodb")
    response = dynamodb.query(
        TableName="main_table",
        KeyConditionExpression="#pk = :pk",
        ExpressionAttributeNames={"#pk": "partition_table"},
        ExpressionAttributeValues={":pk": {"S": "todo"}},
    )
    items = response["Items"]

    return {"todos": items}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=PORT)
