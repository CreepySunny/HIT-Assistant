# ⚾ H.I.T. (Hyper Intelligent Trading) Assistant

**Project Type:** Machine Learning & Sports Analytics  
**Goal:** Project future player performance in batting and pitching  
**Tools:** Python, Jupyter Notebooks, Pandas, Scikit-learn, and more  
**Dataset Range:** MLB player stats from 1871–2014

---

## 📌 Project Overview

H.I.T. Assistant (Hyper Intelligent Trading Assistant) is a machine learning-powered system designed to project the future performance of professional baseball players. It is aimed at providing intelligent trade decision support using historical performance data.

This repository contains two main components:

1. `Batting.ipynb` – Builds and evaluates a predictive model for **batting** performance.
2. `Pitching.ipynb` – Builds and evaluates a predictive model for **pitching** performance.

Each notebook will guide the user through:
- Data loading and preprocessing  
- Exploratory data analysis (EDA)  
- Feature engineering  
- Model building and evaluation  
- Player performance projection

---

## 📁 Repository Structure

```
HIT-Assistant/
│
├── data/
│   ├── Batting.csv
│   ├── Pitching.csv
│
├── batting_projection.ipynb
├── pitching_projection.ipynb
│
└── README.md
```

---

## 📊 Datasets

The data used for this project spans over a century of Major League Baseball (MLB) history and includes statistics, player demographics, and game information.

**Sources:**
- **Lahman Baseball Database (1871–2014)**
- **Chadwick Baseball Bureau Register**
- **Retrosheet Game Logs and Park Codes**

**Location:** All datasets are stored in the `/data` folder.

---

## 🛠 Requirements

- Python 3.8+
- Jupyter Notebook
- pandas
- numpy
- scikit-learn
- matplotlib / seaborn

To install the required packages:

```bash
pip install -r requirements.txt
```

---

## ⚖️ Licensing and Acknowledgments

This work is licensed under a Creative Commons Attribution-ShareAlike 3.0 Unported License.  
For details, see: http://creativecommons.org/licenses/by-sa/3.0/

**Acknowledgments:**
- **Chadwick Baseball Bureau** – Person identification and demographics  
  [http://www.chadwick-bureau.com](http://www.chadwick-bureau.com)

- **Lahman Baseball Database (v2015-01-24)** – Player performance data (1871–2014)  
  Copyright (C) 1996–2015 by Sean Lahman

- **Retrosheet** – Game logs and park code tables  
  [http://www.retrosheet.org](http://www.retrosheet.org)

---

## 🧠 Educational Use

This project is designed for **educational and research purposes**, particularly for those interested in sports analytics, predictive modeling, and machine learning applications in sports.
