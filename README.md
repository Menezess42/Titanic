# Titanic: Kaggle Machine Learning Challenge

This project is an implementation of the classic Titanic survival prediction task from [Kaggle](https://www.kaggle.com/c/titanic). It includes end-to-end data preprocessing, exploratory analysis, feature engineering, and training of several machine learning models for classification.

---

## 🗂 Project Structure

```
Titanic/
├── data/
│   ├── train.csv
│   └── test.csv
│   ├── train_afterEDA.cv
│   ├── test_afterEDA.cv
├── notebooks/
│   ├── EDA.ipynb
│   └── CleaningDATA_and_makePipeline.ipynb
├── submissions/           # Output CSV files for Kaggle submission
│   ├── submission07072025_1.csv
|   ├── ....
|   ├── submission07072025_6.csv
├── flake/                 # Nix flake configuration for reproducible environment
│   └── flake.nix
├── requirements.txt       # Python dependencies
├── .envrc                 # direnv config (optional)
├── .gitignore
└── README.md
```

---

## 💾 Data

1. Download `train.csv` and `test.csv` from the [Kaggle Titanic dataset](https://www.kaggle.com/c/titanic/data).
2. Place them in `data/`.
3. Processed data will be saved automatically in `data/`.

---

## 🛠 Environment Setup

### Using pip

```bash
git clone https://github.com/Menezess42/Titanic.git
cd Titanic
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Using Nix (optional)

```bash
cd Titanic/flake
nix develop
```

This will provide a reproducible development environment with all dependencies.

---

## 🚀 Usage

### 1. Exploratory Data Analysis

Launch the notebook for initial data exploration:

```bash
jupyter notebook notebooks/EDA.ipynb
```

### 2. Model Training & Evaluation

Train and evaluate the following models:

- Gaussian Naive Bayes  
- Logistic Regression  
- Support Vector Classifier (SVC)  
- K‑Nearest Neighbors (KNN)  
- Decision Tree  
- Random Forest  

Open the notebook:

```bash
jupyter notebook notebooks/CleaningDATA_and_makePipeline.ipynb
```

Outputs will be saved in the `submissions/` directory.

---

## 📊 Model Performance

| Model                    | Kaggle Score |
|--------------------------|---------------|
| Gaussian Naive Bayes     | 0.66507       |
| Logistic Regression      | 0.74401       |
| Support Vector Classifier| 0.76076       |
| K‑Nearest Neighbors      | 0.75119       |
| Decision Tree            | 0.65071       |
| Random Forest            | 0.75119       |

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/my-feature`)  
3. Commit your changes  
4. Push to your fork  
5. Open a pull request

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
