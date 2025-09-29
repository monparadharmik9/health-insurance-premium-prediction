# 🏥 Predictive Health Insurance Premium Model

An **AI-powered machine learning web application** developed for **AGI Insurance** by **Apex Technology AI**.  
This project predicts **health insurance premiums** based on user lifestyle, demographic, and medical factors using a trained **Decision Tree model** integrated into a **Flask web app** with a clean HTML interface.  

---  

## 📌 Project Overview  

The capstone project was designed in **two phases**:  

1. **Phase 1 (MVP)** – ✅ Completed  
   - Built and trained a predictive ML model with >67% accuracy.  
   - Developed a Flask-based web application for real-time premium prediction.  
   - Delivered documentation and user training for underwriters.  

2. **Phase 2 (Future Scope)** – 🚀 Planned  
   - Build full infrastructure for **Straight-Through Processing (STP)** of insurance quotes.  
   - Integrate into enterprise insurance systems for automated workflows.  

> This project demonstrates how AI can be **practically applied in insurance** for risk evaluation and premium calculation.  

---  

## 🚀 Features  

- 🌐 **Web-Based Interface**: Simple HTML form for data entry.  
- ⚡ **Fast Predictions**: Flask backend integrates directly with the trained ML model.  
- 🧠 **Decision Tree Model**: Optimized for interpretability and accuracy.  
- 🔐 **Categorical Encoding**: Secure mapping of categorical features to numeric values.  
- 📊 **Accurate Results**: Designed to meet MVP goal — >67% prediction accuracy.  

---  

## 🛠️ Tech Stack  

| Layer            | Tools & Frameworks Used               |  
|------------------|----------------------------------------|  
| Frontend (UI)    | HTML5, CSS3                           |  
| Backend (Server) | Flask (Python Web Framework)          |  
| ML Model         | scikit-learn (Decision Tree Regressor) |  
| Data Handling    | pandas, numpy                         |  
| Notebook         | Jupyter Notebook (EDA + model training)|  

---  

## 🗂️ Project Structure  

```
📁 Predictive_Insurance_Model/
├── app.py                        # Flask backend with prediction route  
├── templates/  
│   └── index.html                # Web form for insurance input data  
├── decision_tree_model.pkl       # Trained ML model (loaded by Flask)  
├── insurance_training.ipynb      # Data preprocessing + model training  
├── requirements.txt              # Dependencies for running the app  
└── README.md                     # Project documentation  
```  

---  

## 📋 Input Features  

| Feature             | Type       | Description                                   |  
|---------------------|------------|-----------------------------------------------|  
| Age                 | Numeric    | Applicant’s age (18–120)                     |  
| Gender              | Categorical| Male / Female                                |  
| Region              | Categorical| Northeast / Northwest / Southeast / Southwest |  
| Marital Status      | Categorical| Married / Unmarried                          |  
| Dependants          | Numeric    | Number of dependants (0–10)                  |  
| BMI Category        | Categorical| Underweight / Normal / Overweight / Obesity  |  
| Smoking Status      | Categorical| No Smoking / Occasional / Regular            |  
| Employment Status   | Categorical| Salaried / Self-Employed / Unemployed        |  
| Income Level        | Categorical| <10L / 10L–25L / 25L–40L / >40L               |  
| Medical History     | Categorical| No Disease / Diabetes / BP / Heart Disease   |  
| Insurance Plan      | Categorical| Bronze / Silver / Gold                       |  

---  

## 🧑‍💻 How to Run Locally  

### 1️⃣ Clone the Repository  

```bash
git clone https://github.com/your-username/Predictive_Insurance_Model.git
cd Predictive_Insurance_Model
```  

### 2️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```  

### 3️⃣ Run the Flask App  

```bash
flask run
```  

Then open your browser at:  
👉 `http://127.0.0.1:5000/`  

You’ll see an **interactive web form** where you can input details and get a predicted premium.  

---  

## 📈 Model Information  

- **Algorithm Used:** Decision Tree Regressor  
- **Target Variable:** Insurance Premium (continuous value)  
- **Training Notebook:** `insurance_training.ipynb`  
- **Evaluation Metrics:** Accuracy goal (>67%), error ≤10% for majority of predictions  
- **Trained Model File:** `decision_tree_model.pkl`  

---  

## 📬 Contact  

- GitHub: [monparadharmik9](https://github.com/monparadharmik9)  
- Email: monparadharmik.9@gmail.com  
- LinkedIn: [Dharmik Monpara](https://linkedin.com/in/dharmik-monpara-data-scientist)  

---  

## ⚠️ Disclaimer  

This project is intended for **educational and demonstration purposes only**.  
It should **not** be used for actual underwriting or insurance pricing in production systems.  

---  

## 🙏 Credits  

- **Client:** AGI Insurance  
- **Service Provider:** Apex Technology AI  
- **Developer:** [Dharmik Monpara]  

---  

✨ A real-world application of **machine learning + Flask** in the **insurance industry** ✨  
