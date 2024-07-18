import streamlit as st 
import pickle 
import joblib
import os
import numpy as np
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Mulitple Diseases Prediction", layout="wide")

working_dir = os.path.dirname(os.path.abspath(__file__))

diabetes_model = pickle.load(open(f'{working_dir}/models/diabetes.pkl', 'rb'))
heart_disease_model = pickle.load(open(f'{working_dir}/models/heart.pkl', 'rb'))
kidney_disease_model = pickle.load(open(f'{working_dir}/models/kidney.pkl', 'rb'))
scaler = scaler = joblib.load(open(f'{working_dir}/models/scaler.pkl', 'rb'))

with st.sidebar:
    selected = option_menu(
        "Disease Detect Pro", 
        [
            'Diabetes Prediction',
            'Heart Disease Prediction',
            'Kidney Disease Prediction'
        ],
        menu_icon = 'hospital-fill',
        icons = ['activity', 'heart', 'person'],
        default_index=0
    ) 


#DIABETES DETECTION
if selected == 'Diabetes Prediction':
    st.markdown("<h1 style = 'text-align: center; color: aqua;'> Predict Diabetes Accurately</h1>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies")

    with col2:
        Glucose = st.text_input("Glucose Level (mg/dL)")

    with col3:
        BloodPressure = st.text_input("Blood Pressure (mm Hg)")

    with col1:
        SkinThickness = st.text_input("Skin Thickness (mm)")

    with col2:
        Insulin = st.text_input("Insulin (mu U/ml)")

    with col3:
        BMI = st.text_input("Body Mass Index (BMI)")

    with col1:
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function")

    with col2:
        Age = st.text_input("Age")

    BMI_Cat_Obesity_1 = 0
    BMI_Cat_Obesity_2 = 0
    BMI_Cat_Obesity_3 = 0
    BMI_Cat_Overweight = 0
    BMI_Cat_Underweight = 0
    Insulin_Cat_Normal = 0
    Glucose_Cat_High = 0
    Glucose_Cat_Low = 0
    Glucose_Cat_Normal = 0


    if st.button("Predict Result"):

        if (float(BMI)<=18.5):
            BMI_Cat_Underweight = 1
        elif (float(BMI)>18.5 and float(BMI)<=24.9):
            pass
        elif (float(BMI)>24.9 and float(BMI)<=29.9):
            BMI_Cat_Overweight = 1
        elif (float(BMI)>29.9 and float(BMI)<=34.9):
            BMI_Cat_Obesity_1 = 1
        elif (float(BMI)>34.9 and float(BMI)<=39.9):
            BMI_Cat_Obesity_2 = 1
        else:
            BMI_Cat_Obesity_3 = 1 
        

        if float(Insulin)>=16 and float(Insulin)<=166:
            Insulin_Cat_Normal = 1
    

        if (float(Glucose)<=70):
            Glucose_Cat_Low = 1
        elif (float(Glucose)>70 and float(Glucose)<=99):
            Glucose_Cat_Normal = 1
        elif (float(Glucose)>99 and float(Glucose)<=126):
            Glucose_Cat_High = 1


        user_input_scale = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, 
                          DiabetesPedigreeFunction, Age]
                          
        user_input_noscale = [BMI_Cat_Obesity_1, BMI_Cat_Obesity_2, BMI_Cat_Obesity_3, BMI_Cat_Overweight, 
                BMI_Cat_Underweight, Insulin_Cat_Normal, Glucose_Cat_High, Glucose_Cat_Low, Glucose_Cat_Normal]
    
        user_input_scale = [float(x) for x in user_input_scale]
        user_input_noscale = [float(x) for x in user_input_noscale]

        user_input_scaled = scaler.transform([user_input_scale])
        user_input_combined = np.hstack((user_input_scaled, np.array(user_input_noscale).reshape(1, -1)))

        prediction = diabetes_model.predict(user_input_combined)

        if prediction[0] == 1:
            diabetes_result = "The person is diabetic"
        else:
            diabetes_result = "The person is not diabetic"

        st.success(diabetes_result)




#HEART DISEASE PREDICTION
if selected == 'Heart Disease Prediction':
    st.markdown("<h1 style = 'text-align: center; color: aqua;'> Predict Heart Disease Accurately</h1>", unsafe_allow_html=True)

    col1, col2, col3  = st.columns(3)

    with col1:
        age = st.text_input("Age")

    with col2:
        sex = st.selectbox("Gender", (
            "Select", "Male", "Female"
            )) 
        
    with col3:
        chestpain = st.selectbox("Chest Pain Type", (
            'Select', 'Asymptomatic', 'Atypical angina', 'Non-anginal pain', 'Typical angina', 
        ))

    with col1:
        restingbp = st.text_input("Resting Blood Pressure (mm Hg)")

    with col2:
        chol = st.text_input("Cholesterol Level (mg/dl)")

    with col3:
        fastingbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", (
            'Select', 'Yes', 'No'
        ))

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', (
            'Select', 'Normal', 'Having ST-T wave abnormality', 'Showing left ventricular hypertrophy'
        ))

    with col2:
        heartrate = st.text_input('Maximum Heart Rate Achieved (bpm)')

    with col3:
        exang = st.selectbox('Exercise Induced Angina',(
            'Select', 'Yes', 'No'
        ))

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.selectbox('Slope of the peak exercise ST segment',(
            'Select', 'Upsloping', 'Flat', 'Downsloping'
        ))

    with col3:
        vessels = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.selectbox('Results of blood flow observed via radioactive dye',(
            'Select', 'Null', 'Normal', 'Fixed defect', 'Reversible defect'
        ))


    if sex == "Male":
        sex = 1
    elif sex == "Female":
        sex = 0


    if chestpain == 'Asymptomatic':
        chestpain = 0
    elif chestpain == 'Atypical angina':
        chestpain = 1
    elif chestpain == 'Non-anginal pain':
        chestpain = 2
    elif chestpain == 'Typical angina':
        chestpain = 3


    if fastingbs == 'Yes':
        fastingbs = 1
    elif fastingbs == 'No':
        fastingbs = 0


    if restecg == 'Showing left ventricular hypertrophy':
        restecg = 0
    elif restecg == 'Normal':
        restecg = 1
    elif restecg == 'Having ST-T wave abnormality':
        restecg = 2


    if exang == 'Yes':
        exang = 1
    elif exang == 'No':
        exang = 0


    if slope == 'Downsloping':
        slope = 0
    elif slope == 'Flat':
        slope = 1
    elif slope == 'Upsloping':
        slope = 2


    if thal == 'Null':
        thal = 0
    elif thal == 'Fixed defect':
        thal = 1
    elif thal == 'Normal':
        thal = 2
    elif thal == 'Reversible defect':
        thal = 3
    
    heart_disease_result = " "


    if st.button("Predict Result"):

        user_input = [age, sex, chestpain, restingbp, chol, fastingbs, restecg, heartrate,
                      exang, oldpeak, slope, vessels, thal]
        
        user_input = [float(x) for x in user_input]
        prediction = heart_disease_model.predict([user_input])

        if prediction[0]==1:
            heart_disease_result = "The person has heart disease"
        else:
            heart_disease_result = "The person does not have heart disease"

        st.success(heart_disease_result)




#KIDNEY DISEASE PREDICTION
if selected == 'Kidney Disease Prediction':
    st.markdown("<h1 style = 'text-align: center; color: aqua;'> Predict Kidney Disease Accurately</h1>", unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        age = st.text_input('Age')

    with col2:
        blood_pressure = st.text_input('Blood Pressure (mm Hg)')

    with col3:
        specific_gravity = st.text_input('Specific Gravity')

    with col4:
        albumin = st.text_input('Albumin (g/dL)')

    with col1:
        sugar = st.text_input('Sugar (mmol/L)')

    with col2:
        red_blood_cells = st.selectbox('Red Blood Cells in Urine',(
            'Select', 'Normal', 'Abnormal'
        ))

    with col3:
        pus_cell = st.selectbox('Pus Cells in Urine',(
            'Select', 'Normal', 'Abnormal'
        ))

    with col4:
        pus_cell_clumps = st.selectbox('Pus Cell Clumps in Urine',(
            'Select', 'Present', 'Not Present'
        ))

    with col1:
        bacteria = st.selectbox('Bacteria in Urine',(
            'Select', 'Present', 'Not Present'
        ))

    with col2:
        blood_glucose_random = st.text_input('Blood Glucose Level (mg/dL)')

    with col3:
        blood_urea = st.text_input('Urea Level in Blood (mg/dL)')

    with col4:
        serum_creatinine = st.text_input('Creatinine Level in Blood (mg/dL)')

    with col1:
        sodium = st.text_input('Sodium Level in Blood (mmol/L)')

    with col2:
        potassium = st.text_input('Potassium Level in Blood (mmol/L)')

    with col3:
        haemoglobin = st.text_input('Haemoglobin Level in Blood (g/dL)')

    with col4:
        packed_cell_volume = st.text_input('Packed Cell Volume (%)')

    with col1:
        white_blood_cell_count = st.text_input('White Blood Cell Count')

    with col2:
        red_blood_cell_count = st.text_input('Red Blood Cell Count')

    with col4:
        hypertension = st.selectbox('Hypertension', (
            'Select', 'Yes', 'No'
        ))

    with col3:
        diabetes_mellitus = st.selectbox('Diabetes Mellitus', (
            'Select', 'Yes', 'No'
        ))

    with col1:
        coronary_artery_disease = st.selectbox('Coronary Artery Disease', (
            'Select', 'Yes', 'No'
        ))

    with col2:
        appetite = st.selectbox('Appetitte', (
            'Select', 'Good', 'Poor'
        ))

    with col3:
        pedal_edema = st.selectbox('Swollen Feet', (
            'Select', 'Yes', 'No'
        ))

    with col4:
        anemia = st.selectbox('Anemia', (
            'Select', 'Yes', 'No'
        ))

    red_blood_cells_normal = 0 
    pus_cell_normal = 0
    pus_cell_clumps_present = 0
    bacteria_present = 0
    hypertension_yes = 0
    diabetes_mellitus_yes = 0
    coronary_artery_disease_yes = 0
    appetite_poor = 0
    pedal_edema_yes = 0
    anemia_yes = 0
    

    if red_blood_cells == 'Normal':
        red_blood_cells_normal = 1
    

    if pus_cell == 'Normal':
        pus_cell_normal = 1


    if pus_cell_clumps == 'Present':
        pus_cell_clumps_present = 1


    if bacteria == 'Present':
        bacteria_present = 1


    if hypertension == 'Yes':
        hypertension_yes = 1


    if diabetes_mellitus == 'Yes':
        diabetes_mellitus_yes = 1


    if coronary_artery_disease == 'Yes':
        coronary_artery_disease_yes = 1


    if appetite == 'Poor':
        appetite_poor = 1


    if pedal_edema == 'Yes':
        pedal_edema_yes = 1


    if anemia == 'Yes':
        anemia_yes = 1

    kindey_disease_result = ' '
   
    if st.button("Predict Result"):

        user_input = [age, blood_pressure, specific_gravity, albumin, sugar, blood_glucose_random, blood_urea, 
                    serum_creatinine, sodium, potassium, haemoglobin, packed_cell_volume, white_blood_cell_count, 
                    red_blood_cell_count, red_blood_cells_normal, pus_cell_normal, pus_cell_clumps_present,
                    bacteria_present, hypertension_yes, diabetes_mellitus_yes, coronary_artery_disease_yes, 
                    appetite_poor, pedal_edema_yes, anemia_yes]

        user_input = [float(x) for x in user_input]
        prediction = kidney_disease_model.predict([user_input])

        if prediction[0] == 0:
            kindey_disease_result = "The person has kidney disease"
        else:
            kindey_disease_result = "The person does not have kidney disease"

        st.success(kindey_disease_result)