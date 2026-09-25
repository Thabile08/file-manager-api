# File Manager API

A simple Flask REST API that uploads, lists, and downloads files from AWS S3
(using MiniStack as a local S3 emulator). Containerized with Docker and deployed
on Kubernetes (Minikube).

## Tools Used

- Python (Flask)
- boto3 (S3 client)
- MiniStack (local S3)
- Docker
- Kubernetes (Minikube)
- Gunicorn

## Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| GET | `/files` | List all files |
| POST | `/upload` | Upload a file |
| GET | `/download/<filename>` | Download a file |

## Run Locally

    # Start MiniStack
    docker run -d -p 4566:4566 --name ministack ministackorg/ministack

    # Create a bucket
    python3 -c "import boto3; s3=boto3.client('s3', endpoint_url='http://localhost:4566', aws_access_key_id='test', aws_secret_access_key='test', region_name='us-east-1'); s3.create_bucket(Bucket='my-bucket')"

    # Install and run
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 app.py

## Build and Deploy on Minikube

    docker build -t file-management-api:latest .
    minikube start
    minikube image load file-management-api:latest
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    minikube service file-api-service --url

## Test the API

    curl <URL>/health
    curl <URL>/files
    curl -X POST -F "file=@requirements.txt" <URL>/upload
    curl -O <URL>/download/requirements.txt

## Author

Thabile — September 2026
