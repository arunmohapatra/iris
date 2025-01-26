
# Iris ML Project - Model Deployment and Orchestration

## Overview

This project involves deploying a machine learning model using Kubernetes and AWS services to predict the Iris dataset classifications. It demonstrates model deployment via API endpoints, orchestration with Kubernetes, and leveraging Helm for ease of deployment.

## Key Features

- **Machine Learning Model Deployment:** The model is deployed as a REST API endpoint.
- **Kubernetes Orchestration:** Utilizes AWS EKS and Helm charts for managing the deployment.
- **Scalability & Fault Tolerance:** The project configures auto-scaling and self-healing features for the model.

## Steps

### 1. Deployed Model Endpoint
The deployed model can be accessed at:
```
POST http://<your-endpoint>/predict
```
Test the endpoint using tools like Postman.

### 2. Kubernetes Configuration and Helm Chart
The Helm chart for deployment is available in the [Helm GitHub repository](https://github.com/arunmohapatra/iris/tree/main/helm).

### 3. AWS EKS Cluster Setup

1. **Create AWS EKS Cluster** using `eksctl`:
```bash
eksctl create cluster --name flask-iris-cluster --region us-east-1 --version 1.27 --nodegroup-name standard-workers --node-type t3.medium --nodes 2 --nodes-min 1 --nodes-max 3 --managed
```

2. **Login to AWS EKS Cluster**:
```bash
aws eks --region us-east-1 update-kubeconfig --name flask-iris-cluster
```

3. **Deploy using Helm**:
```bash
helm install flask-iris ./iris/flask-iris-chart --namespace flask-iris
```

### 4. Cleanup
Delete the EKS cluster using:
```bash
eksctl delete cluster --name flask-iris-cluster
```

## Dependencies

- AWS CLI
- `eksctl`
- Helm
- Kubernetes CLI (kubectl)

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
