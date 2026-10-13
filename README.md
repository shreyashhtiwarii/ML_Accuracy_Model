# Ml_Accuracy_Model

# 🧬 Biomarker-Based Cancer Classification App

This is an interactive Streamlit dashboard designed to classify patients as either **Healthy (1)** or **Cancer (2)** based on their clinical features and biomarkers.

## 📊 Model Information
The app is powered by a **Logistic Regression** model, which achieved the highest test accuracy of **~79.3%** during training evaluation.

### Included Features
*   **Age**
*   **BMI (kg/m²)**
*   **Glucose (mg/dL)**
*   **Insulin (µU/mL)**
*   **HOMA-IR**
*   **Leptin (ng/mL)**
*   **Adiponectin (µg/mL)**
*   **Resistin (ng/mL)**
*   **MCP-1 (pg/mL)**

---

## 🛠️ Local Installation & Execution

1.  **Clone or download** this repository to your local computer.
2.  **Navigate** to the project folder containing the files:
    ```bash
    cd biomarker-cancer-predictor
    ```
3.  **Install dependencies** using `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit application**:
    ```bash
    streamlit run app.py
    ```

---

## 📁 Project Structure
```text
├── app.py                     # Streamlit User Interface script
├── best_logistic_model.pkl    # Serialized Logistic Regression model
├── scaler.pkl                 # Serialized StandardScaler for preprocessing
├── requirements.txt           # Required Python libraries
└── README.md                  # Setup and usage instructions
```

---

## 🚀 Deployment Instructions
To share this app publicly with others, you can deploy it for free using **Streamlit Community Cloud**:

1.  Create a public repository on [GitHub](https://github.com).
2.  Upload `app.py`, `best_logistic_model.pkl`, `scaler.pkl`, `requirements.txt`, and this `README.md` to your repository.
3.  Go to [Streamlit Community Cloud](https://share.streamlit.io/) and log in with your GitHub account.
4.  Click **New App**, select your repository, branch, and set `app.py` as your entry path.
5.  Click **Deploy**! Your app is now live.
