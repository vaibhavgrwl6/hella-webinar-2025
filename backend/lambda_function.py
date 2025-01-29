from flask import Flask, request, jsonify
from mangum import Mangum

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_idea():
    data = request.get_json()
    name = data.get("name")
    idea = data.get("idea")

    # Simulate saving the idea (in real case, store in DynamoDB)
    with open("/tmp/submissions.txt", "a") as file:  # /tmp is writable in AWS Lambda
        file.write(f"{name}: {idea}\n")

    return jsonify({"message": "Idea submitted successfully!"})

# AWS Lambda Entry Point
def lambda_handler(event, context):
    Mangum(app)
