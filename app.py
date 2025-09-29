from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open('decision_tree_model.pkl', 'rb'))
print('Model loaded Successfully')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict_insurance_premium():
    try:
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        region = request.form.get("region")
        marital_status = request.form.get("marital_status")
        dependants = int(request.form.get("dependants"))
        bmi_category = request.form.get("bmi_category")
        smoking_status = request.form.get("smoking_status")
        employment_status = request.form.get("employment_status")
        income_level = request.form.get("income_level")
        medical_history = request.form.get("medical_history")
        insurance_plan = request.form.get("insurance_plan")

        gender_map = {'Male': 0, 'Female': 1}
        region_map = {'Northeast': 0, 'Northwest': 1, 'Southeast': 2, 'Southwest': 3}
        marital_status_map = {'Married': 0, 'Unmarried': 1}
        bmi_category_map = {'Underweight': 0, 'Normal': 1, 'Overweight': 2, 'Obesity': 3}
        smoking_status_map = {'No Smoking': 0, 'Occasional': 1, 'Regular': 2}
        employment_status_map = {'Unemployed': 0, 'Salaried': 1, 'Self-Employed': 2}
        income_level_map = {'<10L': 0, '10L-25L': 1, '25L-40L': 2, '>40L': 3}
        medical_history_map = {'No Disease': 0, 'Diabetes': 1, 'High blood pressure': 2, 'Heart Disease': 3}
        insurance_plan_map = {'Bronze': 0, 'Silver': 1, 'Gold': 2}

        features = [
            age,
            gender_map[gender],
            region_map[region],
            marital_status_map[marital_status],
            dependants,
            bmi_category_map[bmi_category],
            smoking_status_map[smoking_status],
            employment_status_map[employment_status],
            income_level_map[income_level],
            medical_history_map[medical_history],
            insurance_plan_map[insurance_plan],
            0
        ]

        print("Features:", features)

        prediction = model.predict([features])[0]
        print("Raw Prediction:", prediction)

        result = round(prediction)
        return render_template("index.html", prediction=True, result=result)

    except Exception as e:
        print("Error in prediction:", e)
        return render_template("index.html", prediction=False, result="An error occurred during prediction.")


if __name__ == "__main__":
    app.run(debug=True)