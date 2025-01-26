# ML-Ops Assignment 3

## Deliverables

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
  
#### Observations:
- Out of 20 trials, **15 achieved perfect accuracy** (1.0000), indicating multiple configurations worked well.
- The best configuration achieved perfect accuracy with moderate parameter values:
  - `n_estimators = 132`
  - `max_depth = 36`
- Some configurations with extreme parameter values (e.g., `max_depth = 2` or `n_estimators = 196`) resulted in slightly lower accuracy (**0.9917**), suggesting potential overfitting or underfitting.

#### Conclusion:
The tuning process successfully identified optimal hyperparameters, resulting in a highly accurate Random Forest Classifier. The model is robust and ready for deployment with the chosen hyperparameters.

---

### 2. Docker and Flask Application
- **Dockerfile**: [View Dockerfile](https://github.com/arunmohapatra/iris/blob/main/Dockerfile)
- **Flask Application Code**: [View Flask Application](https://github.com/arunmohapatra/iris/blob/main/app.py)
- **Complete Code Base**: [GitHub Repository](https://github.com/arunmohapatra/iris)

#### Docker Hub:
The container image is available on Docker Hub:  
[Docker Hub Link](https://hub.docker.com/r/arunbits/flask-app)

---

### 3. Running the Dockerized Application

#### Steps to Run the Docker Container:
1. **Start Docker**:
   - Open Docker Desktop and ensure it is running.

2. **Pull and Run the Docker Image**:
   ```bash
   docker run -p 5000:5000 arunbits/flask-app:latest

