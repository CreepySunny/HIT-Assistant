# ⚾ H.I.T. (Hyper Intelligent Trading) Assistant

**Project Type:** Machine Learning & Sports Analytics  
**Goal:** Project future player performance in batting and pitching  
**Tools:** Python, Jupyter Notebooks, Pandas, Scikit-learn, and more  
**Dataset Range:** MLB player stats from 1871–2014

---

## 📌 Project Overview

H.I.T. Assistant (Hyper Intelligent Trading Assistant) is a machine learning-powered system designed to project the future performance of professional baseball players. It is aimed at providing intelligent trade decision support using historical performance data.

This repository contains the following main components:

- `HRpAB.ipynb` – Builds and evaluates a predictive model for **batting** performance (Home Runs per At-Bat).
- `mcp_server.py` – MCP-compliant server exposing the trained model for compliant, auditable predictions.
- `random_forest.pkl` – Trained Random Forest model used by the MCP server.
- `data/` – Contains all datasets (e.g., `Batting.csv`).
- `requirements.txt` – All Python dependencies.
- `README.md` – Project documentation and setup instructions.

---

## 📁 Repository Structure

```
repo/
│
├── data/
│   └── Batting.csv
│
├── HRpAB.ipynb
├── mcp_server.py
├── random_forest.pkl
├── requirements.txt
├── README.md
├── .gitignore
└── .venv/ (optional, if using a virtual environment)
```

---

## 🛠 Installation & Setup

1. **Clone the repository:**

   ```bash
   git clone <repo-url>
   cd repo
   ```

2. **Install Python dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **(Optional) Set up a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

4. **Download datasets:**
   - Ensure `data/Batting.csv` is present. Other datasets may be required for additional notebooks.

5. **Run Jupyter Notebooks:**

   ```bash
   jupyter notebook
   # Open HRpAB.ipynb or Batting wOBA.ipynb in your browser
   ```

6. **Run the MCP Server:**

   ```bash
   python mcp_server.py
   ```
   - The server exposes the trained model for compliant, auditable predictions.

---

## 📊 Datasets

The data used for this project spans over a century of Major League Baseball (MLB) history and includes statistics, player demographics, and game information.

**Sources:**
- **Lahman Baseball Database (1871–2014)**
- **Chadwick Baseball Bureau Register**
- **Retrosheet Game Logs and Park Codes**

**Location:** All datasets are stored in the `/data` folder.

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
