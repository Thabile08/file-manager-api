WTC CODE : WTC-S5LQ9TKR

# S3 File Management API on Kubernetes

A simple REST API built with **Python (Flask)** that uploads, lists, and downloads files from **AWS S3**. The app is containerized with **Docker** and deployed on **Kubernetes (Minikube)**.

---

## Features

- Upload files to an S3 bucket
- List all files in the bucket
- Download files using pre-signed URLs
- Health check endpoint
- Runs on Kubernetes with 2 replicas

---

## Tech Stack

- Python 3.9 + Flask
- AWS S3 (boto3)
- Docker
- Kubernetes (Minikube)

---

## Project Structure

s3-file-api/
├── app/
│ ├── main.py
│ └── requirements.txt
├── k8s/
│ ├── secret.yaml
│ ├── configmap.yaml
│ ├── deployment.yaml
│ └── service.yaml
├── Dockerfile
└── README.md

