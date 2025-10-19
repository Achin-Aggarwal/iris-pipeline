# 🌸 Iris ML Pipeline

This repository implements an **end-to-end machine learning pipeline** for the classic **Iris dataset**, integrated with **DVC for data & model versioning** and **GitHub Actions for CI/CD**.  

It is part of an academic assignment to demonstrate:
- Data version control with **DVC + Google Cloud Storage**
- Model training and evaluation
- Unit testing with **pytest**
- Continuous Integration (CI) with **GitHub Actions**
- Automated reporting using **CML** (Continuous Machine Learning)

---

## 🚀 Features
- **DVC Integration**  
  Dataset and model artifacts are tracked via DVC and stored in a Google Cloud Storage (GCS) bucket.

- **CI/CD with GitHub Actions**  
  - Runs tests automatically on every push/PR to `main` and `dev`
  - Pulls dataset/model artifacts via DVC
  - Publishes evaluation/test reports as PR comments with CML

- **Unit Tests**  
  Implemented with `pytest` to validate:
  - Data integrity
  - Model performance (sanity checks)
  - Evaluation metrics

- **Branching Strategy**  
  - `dev` branch for development  
  - `main` branch for production-ready code

---

## 🏗️ Project Structure

