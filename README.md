# **Credit Risk ML System**

End-to-end Machine Learning system for predicting credit score categories:
- Good
- Standard
- Poor

Includes:
- Model training pipeline
- Inference service (FastAPI)
- Frontend UI
- Database logging (SQLite)
- Dockerized deployment

---

# Features

 - ML Pipeline (Scikit-learn)  
 -  Feature Engineering  
 - REST API (FastAPI)  
 - Interactive UI (HTML/CSS/JS)  
 - Prediction confidence  
 - SQLite logging  
 - Docker & Docker Compose  

---

# Project Structure
```
/credit-risk-ml-system/
|--data/ 
|  |--raw/
|     |     |--.gitkeep
|     |     |--Credit_score_cleaned_data.csv
|  |--processed/
|     |     |--X_test.csv
|     |     |--X_train.csv
|     |     |--X_val.csv
|     |     |--y_test.csv
|     |     |--y_train.csv
|     |     |--y-val.csv
|--models/
|     |--pipeline.pkl
|--notebooks/
|     |--data_preprocessing.ipynb
|     |--eda.ipynb
|     |--modeling.ipynb
|--src/
|     |--api/
|     |--database/
|     |--inference/
|     |--services/
|     |--training/
|     |--utils/
|--ui/
|     |--index.html
|     |--script.js
|     |--style.css
|--venv
|--docker-compose.yml
|--Dockerfile
|--.gitignore
|--README.MD
|--requirements.txt
|--run_api.sh
```

# Installation commands 

## 1. Clone repository
```bash
git clone https://github.com/aidartakenov/credit-risk-ml-system.git
cd credit-risk-ml-system
```

## 2. Create virtual environment
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```
## 3. You can install dependencies with:
```
pip install -r requirements.txt
```
## 4. You can train the model with:
```
python -m src.training.train
```
## 5. You can run the test with:
```
python -m src.inference.inference
```

# Running the API
    You can run the api with:
```
python -m src.inference.inference
```
and open the Swagger UI with the link:
```
http://127.0.0.1:8000/docs
```

# Running the UI
    You can run the UI:
```
cd ui
python -m http.server 5500
```
and open in the browser with the link:
```
http://localhost:5500
```

# Database
For svaing the prediction results I used SQLite.
It stores input data, prediction, confidence.
File: ```data/predictions.db```
However, all the database files were gitignored.

# Docker
You can build and run docker with:
```
docker compose up --build
```





## Dataset

Download the dataset from the link:
https://drive.google.com/file/d/1GcTLyas1eowSrbnAwmfSntlriGEaVeH_/view?usp=drive_link

Place the file in:
data/raw/Credit_score_cleaned_data.csv
