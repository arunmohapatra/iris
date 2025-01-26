# M3: Model Experimentation and Packaging

**Objective**: Train a machine learning model, perform hyperparameter tuning, and package the model for deployment.

### 1. Hyperparameter Tuning Report
- **Objective**: Optimize the hyperparameters of a Random Forest Classifier to achieve the highest possible accuracy.
- **Report**: [Hyperparameter Tuning Report](https://github.com/arunmohapatra/iris/blob/main/tuning_report.txt)

#### Best Parameters:
- `n_estimators`: 132
- `max_depth`: 36
- `min_samples_split`: 17

#### Best Accuracy:
- **1.0000**

#### Summary of the Tuning Process:
- Evaluated **20 trials** with different combinations of `n_estimators`, `max_depth`, and `min_samples_split`.
- The **optimal configuration (Trial 0)** achieved a perfect accuracy of **1.0000**, demonstrating the model's capability to perfectly classify the dataset.
### Performance of All Trials:
![image](https://github.com/user-attachments/assets/158ea50c-863e-41b1-b20c-efa691a3a276)

#### Observations:
- Out of 20 trials, **15 achieved perfect accuracy** (1.0000), indicating multiple configurations worked well.
- The best configuration achieved perfect accuracy with moderate parameter values:
  - `n_estimators = 132`
  - `max_depth = 36`
- Some configurations with extreme parameter values (e.g., `max_depth = 2` or `n_estimators = 196`) resulted in slightly lower accuracy (**0.9917**), suggesting potential overfitting or underfitting.

#### Conclusion:
The tuning process successfully identified optimal hyperparameters, resulting in a highly accurate Random Forest Classifier. The model is robust and ready for deployment with the chosen hyperparameters.


### 2. Docker and Flask Application
- **Dockerfile**: [View Dockerfile](https://github.com/arunmohapatra/iris/blob/main/Dockerfile)
- **Flask Application Code**: [View Flask Application](https://github.com/arunmohapatra/iris/blob/main/src/app.py)
- **Complete Code Base**: [GitHub Repository](https://github.com/arunmohapatra/iris)

#### Docker Hub:
The container image is available on Docker Hub:  [Docker Hub Link](https://hub.docker.com/r/arunbits/flask-app)

![image](https://github.com/user-attachments/assets/639f51ec-918d-4f32-9bfd-8f87a49b7490)


### 3. Running the Dockerized Application

#### Steps to Run the Docker Container:
1. **Start Docker**:
   - Open Docker Desktop and ensure it is running.
     ![image](https://github.com/user-attachments/assets/e9ee584f-7b29-4cb2-a0e9-91ade13999bd)
   - Once docker desktop is ready and running you can run docker command and verify the version of docker
     ![image](https://github.com/user-attachments/assets/08d6da95-0453-4d36-b3ab-cc22e336c2b8)


2. **Pull and Run the Docker Image**:

   docker run -p 5000:5000 arunbits/flask-app:latest

   ![image](https://github.com/user-attachments/assets/6c6561fc-c41c-44d5-84a4-3428b2ef2dfd)


   Verify docker container is running
   ![image](https://github.com/user-attachments/assets/512b9829-b72b-4ac6-b86c-306bf9272025)

    Verify the docker image from docker desktop UI console

    ![image](https://github.com/user-attachments/assets/6380a384-af5a-4a91-b2a5-662a95e1a43f)

    Running container
    ![image](https://github.com/user-attachments/assets/e3cfecf5-784a-4650-a330-f7483e6f83fb)

    Execute the prediction API from postman
   
    ![image](https://github.com/user-attachments/assets/5a2dbcbc-de77-48b7-88e7-9fc649261fb3)
