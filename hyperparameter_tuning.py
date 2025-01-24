import optuna
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
import pickle

# Load dataset from Iris.csv
def load_data():
    # Load the dataset from the CSV file
    df = pd.read_csv("Iris.csv")

    # Assuming the last column is the target (species)
    X = df.iloc[:, :-1].values  # Feature columns
    y = df.iloc[:, -1].astype("category").cat.codes.values  # Convert target to numeric

    return train_test_split(X, y, test_size=0.2, random_state=42)

# Objective function for Optuna
def objective(trial):
    n_estimators = trial.suggest_int("n_estimators", 10, 200)
    max_depth = trial.suggest_int("max_depth", 2, 50)
    min_samples_split = trial.suggest_int("min_samples_split", 2, 20)

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        min_samples_split=min_samples_split,
        random_state=42
    )
    scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")
    return scores.mean()

# Main function
if __name__ == "__main__":
    # Split data
    X_train, X_test, y_train, y_test = load_data()

    # Run Optuna optimization
    study = optuna.create_study(direction="maximize")
    study.optimize(objective, n_trials=20)
    print("Best Parameters:", study.best_params)

    # Train model with best parameters
    best_model = RandomForestClassifier(**study.best_params, random_state=42)
    best_model.fit(X_train, y_train)

    # Save the model as model.pkl
    with open("model.pkl", "wb") as f:
        pickle.dump(best_model, f)

    print("Model saved as model.pkl")
