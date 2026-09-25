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

    docker run -d -p 4566:4566 --name ministack ministackorg/ministack
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python3 app.py

## Deploy on Minikube

    docker build -t file-management-api:latest .
    minikube start
    minikube image load file-management-api:latest
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
    minikube service file-api-service --url

WTC Code: WTC-S5LQ9TKR

## Author

Thabile — September 2026
