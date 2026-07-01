# DevOps-Flask-Pulimi-Example
Cloned and modified with thanks from https://github.com/Thejashree-s/devops-python-webapp.git

## 🚀 Overview
This repository contains a simple Python Flask web application demonstrating DevOps practices:
- Containerization with Docker
- CI/CD using GitHub Actions
- Deployment infrastructure with Pulimi on AWS

## 🛠️ Technologies Used
- **Python**: Flask Web App
- **Docker**: Containerization
- **GitHub Actions**: CI/CD
- **Pulimi**: Infrastructure as Code
- **AWS**: EC2 deployment

## 📂 Project Structure

/app
/.github/workflows
/pulimi
README.md

## 🔧 Getting Started
1. Clone the repository:
```bash
git clone https://github.com/Thejashree-s/devops-python-webapp.git

2. Build Docker image:
cd app
docker build -t devops-flask-app .
docker run -p 5000:5000 devops-flask-app

3. Pulimi:
cd pulimi
pulimi up

## 📄 License
MIT License
```
