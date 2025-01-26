
# ML-Ops Assignment 4

## Deliverables

### 1. Deployed Model Endpoint
The machine learning model is deployed and accessible via the following endpoint:

**Endpoint**:
```http
POST http://a1e979fcdfbec4aba8e310441af6d15a-2108912047.us-east-1.elb.amazonaws.com:80/predict
```

You can verify the model using **Postman** or any other API testing tool.

![image](https://github.com/user-attachments/assets/59e96666-92d1-4167-b04b-1f7c034e439b)


### 2. Kubernetes Configuration and Helm Chart
The Kubernetes configuration files and Helm chart used for deployment can be found in the following GitHub repository: https://github.com/arunmohapatra/iris/tree/main/helm

![image](https://github.com/user-attachments/assets/9405ad36-2629-425e-bb91-568a055583cc)


### 3. Deployment and Orchestration Process

#### Creation of AWS EKS Cluster
Follow these steps to create an **AWS EKS Cluster**:

1. **Login to AWS Account**:
   Use the AWS CLI to log in:
   ```bash
   aws configure
   ```
   ![image](https://github.com/user-attachments/assets/2180ff38-ccff-4c1c-97d3-70b2cee9f2f0)

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
   ![image](https://github.com/user-attachments/assets/4d9cb576-1a81-48d9-9b7c-e8870b80931b)
   ![image](https://github.com/user-attachments/assets/b3d32c1c-619f-41e9-a1bc-b1316289e319)
   ![image](https://github.com/user-attachments/assets/aa55d1cd-2f0a-4e77-83fd-4ae3d64fdd2a)
   ![image](https://github.com/user-attachments/assets/c66d06d7-e309-48aa-8c51-890e05f1f0ab)

4. **Verify the Cluster**:
   Once created, verify the cluster in the AWS Management Console.  
   **Cluster Name**: `flask-iris-cluster`

   ![image](https://github.com/user-attachments/assets/7bedbf36-d801-4507-9aa5-7c62ceecf3dd)


#### Login to AWS EKS Cluster

1. **Update kubeconfig**:
   Use the following command to connect to the newly created cluster:
   ```bash
   aws eks --region us-east-1 update-kubeconfig --name flask-iris-cluster
   ```
   ![image](https://github.com/user-attachments/assets/90cb79c6-5f0f-41da-8ac4-030ae6ffd877)

2. **Create a Namespace**:
   Create a namespace within the cluster:
   ```bash
   kubectl create namespace flask-iris
   ```
   ![image](https://github.com/user-attachments/assets/94ef1498-b488-4630-8254-b0f5231d0631)

3. **Verify Namespace**:
   Check if the namespace was created successfully:
   ```bash
   kubectl get namespace
   ```
   ![image](https://github.com/user-attachments/assets/6fd710ad-7cf3-4231-8af3-ae408f5c29e7)

#### Deployment Using Helm

1. **Install Helm CLI**:
   Ensure Helm is installed on your system.
2. **Deploy the Service**:
   Use the following Helm command to deploy the service:
   ```bash
   helm install flask-iris ./iris/flask-iris-chart --namespace flask-iris
   ```
   
   ![image](https://github.com/user-attachments/assets/dbecc3eb-b234-4c32-bb5f-548e454a19dd)

   
4. **Check Service and Deployment Status**:
   Verify the deployment and service status with:
   ```bash
   kubectl get svc -n flask-iris
   ```
   ![image](https://github.com/user-attachments/assets/6780e1e5-99f4-4b52-8296-882ce6c3feef)
   ![image](https://github.com/user-attachments/assets/fbc47240-089b-4e2c-baad-55550bbb911d)
   ![image](https://github.com/user-attachments/assets/0d111988-efbe-4d66-9f0a-c123479ac0c3)
   ![image](https://github.com/user-attachments/assets/53733600-ab02-43be-8b07-2d917468c4d6)
   ![image](https://github.com/user-attachments/assets/9f0ffe8a-76cb-40be-a897-e191b50ded0c)

   

#### Destroying the EKS Cluster
To clean up resources and delete the EKS cluster, use:
```bash
eksctl delete cluster --name flask-iris-cluster
```
     ![image](https://github.com/user-attachments/assets/c764b7f9-e5e2-4f21-8a56-e6a95672bd25)

