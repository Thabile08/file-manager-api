import os
from flask import Flask, request, jsonify, send_file
import boto3
from botocore.exceptions import NoCredentialsError
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION = os.getenv('AWS_REGION', 'us-east-1')
S3_BUCKET = os.getenv('S3_BUCKET_NAME')
S3_ENDPOINT_URL = os.getenv('S3_ENDPOINT_URL')  # None = real AWS

s3_client = boto3.client(
    's3',
    endpoint_url=S3_ENDPOINT_URL,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

@app.route('/health')
def health():
    return "OK", 200

@app.route('/files', methods=['GET'])
def list_files():
    try:
        response = s3_client.list_objects_v2(Bucket=S3_BUCKET)
        files = [obj['Key'] for obj in response.get('Contents', [])]
        return jsonify({'files': files})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    try:
        s3_client.upload_fileobj(file, S3_BUCKET, file.filename)
        return jsonify({'message': f'File {file.filename} uploaded successfully'}), 200
    except NoCredentialsError:
        return jsonify({'error': 'AWS credentials not available'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_obj = s3_client.get_object(Bucket=S3_BUCKET, Key=filename)
        return send_file(file_obj['Body'], as_attachment=True, download_name=filename)
    except s3_client.exceptions.NoSuchKey:
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
