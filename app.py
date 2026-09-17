import boto3
from flask import Flask, jsonify, render_template
from botocore.exceptions import NoCredentialsError, PartialCredentialsError


app = Flask(__name__)

s3_client = boto3.client('s3')


@app.get("/")
def index():
    return jsonify(message="Flask is running")


@app.get("/health")
def health():
    return jsonify(status="ok")


@app.get("/firemap")
def firemap():
    img_name = "fire_video.gif"

    try:
        # Create S3 link
        img_url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': 'co_fires_video', 'Key': img_name},
            ExpiresIn=3600  # Link expiration time in seconds
        )
        return render_template("firemap.html", img_url=img_url)
    except (NoCredentialsError, PartialCredentialsError):
        return jsonify(error="AWS credentials not found or incomplete"), 500


@app.get("/musician_graph")
def musician_graph():
    pass


@app.get("/hayman_map")
def hayman_map():
    pass


@app.get("/drums_and_cymbals")
def drums_and_cymbals():
    pass
