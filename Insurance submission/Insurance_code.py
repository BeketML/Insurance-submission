import streamlit as st
import joblib

def load_model():
    # Загрузка модели из файла
    model = joblib.load('C:/Users/ASUS/Desktop/1-pet/model_joblib_gb')
    return model

def show_prediction(model, age, sex, bmi, children, smoker, region):
    # Делаем предсказание
    prediction = model.predict([[age, sex, bmi, children, smoker, region]])
    return prediction

def main():
    st.title("Health Insurance Cost Prediction")

    # Входные данные пользователя
    age = st.number_input("Enter Your Age", min_value=18, max_value=100, value=30)
    sex_input = st.selectbox("Male or Female", ("Male", "Female"))
    sex = 1 if sex_input == "Male" else 0
    
    bmi = st.number_input("Enter Your BMI Value")
    children = st.number_input("Enter number of your Children [1-4]", min_value=0, max_value=10, value=0)
    
    smoker_input = st.selectbox("Smoker", ("Yes", "No"))
    smoker = 1 if smoker_input == "Yes" else 0

    region_input = st.selectbox("Region", ("northeast", "northwest", "southeast", "southwest"))
    if region_input == "northeast":
        region = 1
    elif region_input == "northwest":
        region = 2
    elif region_input == "southeast":
        region = 3
    else:
        region = 4

    model = load_model()

    if st.button("Predict"):
        prediction = show_prediction(model, age, sex, bmi, children, smoker, region)
        st.success(f"Estimated Insurance Cost: ${prediction[0]}")

if __name__ == "__main__":
    main()




    


