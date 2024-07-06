import pickle 
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved model 

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

breast_cancer_model = pickle.load(open('breast_cancer_model.sav', 'rb'))


# sidebar for navigate 

with st.sidebar:

    selected = option_menu('Multiple Disease Prediction System',
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],

                            icons = ['activity', 'heart', 'person', 'gender-female'],

                            default_index=0)  #starting page is Diabetes Prediction first index[0]
    

# Diabetes Prediction page
if (selected == 'Diabetes Prediction'):

    #page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3) 

    with col1: 
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col2:
        Age = st.text_input('Age of the Person')
    
    
    
    # code for prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]]) #[[]] --> model predicts for only one person's data

        if (diab_prediction[0] == 1):
            diab_diagnosis = 'The pereson is Diabetic'

        else:
            diab_diagnosis = 'The pereson is Not Diabetic'
    
    st.success(diab_diagnosis)



if (selected == 'Heart Disease Prediction'):

    #page title
    st.title('Heart Disease Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3 = st.columns(3) 

    with col1: 
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain type')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results')

    with col2:
        thalach = st.text_input('Maximum heart rate achieved')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST Depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    
    
    
    # code for prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), float(cp), float(trestbps), float(chol), float(fbs), float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])      #[[]] --> model predicts for only one person's data

        if (heart_prediction[0] == 1):
            heart_diagnosis = 'The Person has Heart Disease'
        
        else:
            heart_diagnosis = 'The Person does not have a Heart Disease'


    
    st.success(heart_diagnosis)



if (selected == 'Parkinsons Prediction'):

    #page title
    st.title('Parkinsons Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3, col4= st.columns(4) 

    with col1: 
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col1:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col2:
        RAP = st.text_input('MDVP:RAP')

    with col3:
        PPQ = st.text_input('MDVP:PPQ')

    with col4:
        DDP = st.text_input('Jitter:DDP')
    
    with col1:
        Shimmer = st.text_input('MDVP:Shimmer')
    
    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col4:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col1:
        APQ = st.text_input('MDVP:APQ')
        
    with col2:
        DDA = st.text_input('Shimmer:DDA')
        
    with col3:
        NHR = st.text_input('NHR')
        
    with col4:
        HNR = st.text_input('HNR')
        
    with col1:
        RPDE = st.text_input('RPDE')
        
    with col2:
        DFA = st.text_input('DFA')
        
    with col3:
        spread1 = st.text_input('spread1')
        
    with col4:
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
    
    
    
    # code for prediction
    parkinson_diagnosis = ''

    # creating a button for Prediction

    if st.button("Parkinson's Test Result"):
        parkinson_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]]) #[[]] --> model predicts for only one person's data

        if (parkinson_prediction[0] == 1):
            parkinson_diagnosis = "The person has Parkinson's disease"

        else:
            parkinson_diagnosis = "The person does not have Parkinson's disease"
    
    st.success(parkinson_diagnosis)



if (selected == 'Breast Cancer Prediction'):

    #page title
    st.title('Breast Cancer Prediction using ML')

    # getting the input data from the user
    # columns for input fields
    col1, col2, col3, col4 = st.columns(4) 

    with col1: 
        mean_radius = st.text_input('Mean Radius')

    with col2:
        mean_texture = st.text_input('Mean Texture')

    with col3:
        mean_perimeter = st.text_input('Mean Perimeter')

    with col4:
        mean_area = st.text_input('Mean Area')

    with col1:
        mean_smoothness = st.text_input('Mean Smoothness')

    with col2:
        mean_compactness = st.text_input('Mean Compactness')

    with col3:
        mean_concavity = st.text_input('Mean Concavity')

    with col4:
        mean_concave_points = st.text_input('Mean Concave Points')

    with col1:
        mean_symmetry = st.text_input('Mean Symmetry')
    
    with col2:
        mean_fractal_dimension = st.text_input('Mean Fractal Dimension')
    
    with col3:
        radius_error = st.text_input('Radius Error')

    with col4:
        texture_error = st.text_input('Texture Error')
        
    with col1:
        perimeter_error = st.text_input('Perimeter Error')
        
    with col2:
        area_error = st.text_input('Area Error')
        
    with col3:
        smoothness_error = st.text_input('Smoothness Eerror')
        
    with col4:
        compactness_error = st.text_input('Compactness Error')
        
    with col1:
        concavity_error = st.text_input('Concavity Error')
        
    with col2:
        concave_points_error = st.text_input('Concave Points Error')
        
    with col3:
        symmetry_error = st.text_input('Symmetry Error')
        
    with col4:
        fractal_dimension_error = st.text_input('Fractal Dimension Error')
        
    with col1:
        worst_radius = st.text_input('Worst Radius')
        
    with col2:
        worst_texture = st.text_input('Worst Texture')
        
    with col3:
        worst_perimeter = st.text_input('Worst Perimeter')

    with col4:
        worst_area = st.text_input('Worst Area')
        
    with col1:
        worst_smoothness = st.text_input('Worst Smoothness')
        
    with col2:
        worst_compactness = st.text_input('Worst Compactness')

    with col3:
        worst_concavity = st.text_input('Worst Concavity')
        
    with col4:
        worst_concave_points = st.text_input('Worst Concave Points')

    with col1:
        worst_symmetry = st.text_input('Worst Symmetry')
        
    with col2:
        worst_fractal_dimension = st.text_input('Worst Factal Dimension')
        
    
    
    
    # code for prediction
    cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Breast Cancer Test Result'):
        cancer_prediction = breast_cancer_model.predict([[float(mean_radius), float(mean_texture), float(mean_perimeter), float(mean_area), float(mean_smoothness), float(mean_compactness), float(mean_concavity), float(mean_concave_points), float(mean_symmetry), float(mean_fractal_dimension), float(radius_error), float(texture_error), float(perimeter_error), float(area_error), float(smoothness_error), float(compactness_error), float(concavity_error), float(concave_points_error), float(symmetry_error), float(fractal_dimension_error), float(worst_radius), float(worst_texture), float(worst_perimeter), float(worst_area), float(worst_smoothness), float(worst_compactness), float(worst_concavity), float(worst_concave_points), float(worst_symmetry), float(worst_fractal_dimension)]]) #[[]] --> model predicts for only one person's data

        if (cancer_prediction[0] == 1):
            cancer_diagnosis = 'The breast cancer is Benign'

        else:
            cancer_diagnosis = 'The breast cancer is Malignant'
    
    st.success(cancer_diagnosis)