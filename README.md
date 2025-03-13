# Flask Microservice Project

## Overview
This project is a simple Flask microservice with CRUD operations, designed for containerization and deployment in a secure CI/CD pipeline.

## Features
- RESTful API with CRUD operations
- Docker support (Dockerfile)
- CI/CD pipeline with GitHub Actions
- Security scanning (Snyk, Trivy, GitHub Dependabot, etc.)
- Unit tests with Pytest
- Kubernetes deployment configuration

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/flask-microservice.git
   cd flask-microservice
   ```

2. **Create a Virtual Environment & Install Dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

## Running the Microservice

Run the Flask application locally:
```bash
python app.py
```

The service will be available at `http://127.0.0.1:5000/`.

## Docker Setup

1. **Build the Docker Image:**
   ```bash
   docker build -t flask-microservice .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 5000:5000 flask-microservice
   ```

## CI/CD Pipeline (GitHub Actions)

This project includes automated testing and security scanning using GitHub Actions. The pipeline runs on every push/commit and includes:
- **Code Scanning:** Using **CodeQL**
- **Dependency Security:** Using **Snyk** and **OWASP Dependency-Check**
- **Container Scanning:** Using **Trivy**
- **Automated Testing:** Using **Pytest**

## Kubernetes Deployment

1. **Apply Kubernetes Configurations:**
   ```bash
   kubectl apply -f k8s/deployment.yaml
   kubectl apply -f k8s/service.yaml
   ```

2. **Check Deployment Status:**
   ```bash
   kubectl get pods
   ```

## API Endpoints

| Method | Endpoint        | Description            |
|--------|----------------|------------------------|
| GET    | `/`            | Welcome message       |
| GET    | `/items`       | Retrieve all items    |
| POST   | `/items`       | Add a new item        |
| PUT    | `/items/<id>`  | Update an item        |
| DELETE | `/items/<id>`  | Delete an item        |

## Security Measures

- **Automated security testing in GitHub Actions**
- **Fails the build if vulnerabilities are detected**
- **Scans for hardcoded secrets and vulnerabilities**
- **Container security scanning before deployment**

## Next Steps
- **Integrate Infrastructure as Code (IaC) security scanning**
- **Set up policy enforcement for Kubernetes**
- **Monitor vulnerabilities post-deployment with tools like Falco**

---

### 🚀 Secure & Scalable Flask Microservice Ready!
Use this guide to build, test, and deploy your Flask microservice securely.

