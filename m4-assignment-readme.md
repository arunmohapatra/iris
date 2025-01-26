
# ML-Ops Assignment 4

## Deliverables

### 1. Deployed Model Endpoint
The machine learning model is deployed and accessible via the following endpoint:

**Endpoint**:
```http
POST http://a1e979fcdfbec4aba8e310441af6d15a-2108912047.us-east-1.elb.amazonaws.com:80/predict
```

You can verify the model using **Postman** or any other API testing tool.



### 2. Kubernetes Configuration and Helm Chart
The Kubernetes configuration files and Helm chart used for deployment can be found in the following GitHub repository: https://github.com/arunmohapatra/iris/tree/main/helm


### 3. Deployment and Orchestration Process

#### Creation of AWS EKS Cluster
Follow these steps to create an **AWS EKS Cluster**:

1. **Login to AWS Account**:
   Use the AWS CLI to log in:
   ```bash
   aws configure
   ```

2. **Install eksctl CLI**:
   - If `eksctl` is not already installed, follow the instructions to install it from the [AWS EKS eksctl documentation](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html).

3. **Create the EKS Cluster**:
   Run the following command to create the cluster:
   ```bash
   eksctl create cluster \
     --name flask-iris-cluster \
     --region us-east-1 \
     --version 1.27 \
     --nodegroup-name standard-workers \
     --node-type t3.medium \
     --nodes 2 \
     --nodes-min 1 \
     --nodes-max 3 \
     --managed
   ```

4. **Verify the Cluster**:
   Once created, verify the cluster in the AWS Management Console.  
   **Cluster Name**: `flask-iris-cluster`



#### Login to AWS EKS Cluster

1. **Update kubeconfig**:
   Use the following command to connect to the newly created cluster:
   ```bash
   aws eks --region us-east-1 update-kubeconfig --name flask-iris-cluster
   ```

2. **Create a Namespace**:
   Create a namespace within the cluster:
   ```bash
   kubectl create namespace flask-iris
   ```

3. **Verify Namespace**:
   Check if the namespace was created successfully:
   ```bash
   kubectl get namespace
   ```



#### Deployment Using Helm

1. **Install Helm CLI**:
   Ensure Helm is installed on your system.

2. **Deploy the Service**:
   Use the following Helm command to deploy the service:
   ```bash
   helm install flask-iris ./iris/flask-iris-chart --namespace flask-iris
   ```

3. **Check Service and Deployment Status**:
   Verify the deployment and service status with:
   ```bash
   kubectl get svc -n flask-iris
   ```



#### Destroying the EKS Cluster
To clean up resources and delete the EKS cluster, use:
```bash
eksctl delete cluster --name flask-iris-cluster
```

