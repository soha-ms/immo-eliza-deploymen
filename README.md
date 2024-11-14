# immo-eliza-deployment 🏠
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white)


## 🏢 Description
This project aims to deploy a machine learning model to predict property prices through an API endpoint. It also includes a streamlit web application for easier interaction with the model. The project is structured into two main parts: 
 - The API for developers 
 -  User-friendly web application for non-technical users. 

## Repo structure
```
├── api/
│   ├── app.py
│   ├── predict.py   
│   ├── xgb_model.joblib [Saved model]  
├── streamlit/
│   ├── streamlit.py
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt

```

## 🚀 Deployment

The FastAPI backend is deployed on Render, containerized with Docker
and the Streamlit runs locally through cmd prompt 

## 🛎️ Usage

1. Clone the repository to your local machine.

    https://github.com/soha-ms/immo-eliza-deployment.git

2. Navigate to the project  directory, install the required dependencies:
    
    pip install -r requirements.txt
 
3. Navigate to the project streamlit directory and run below command:
    
    streamlit run streamlit.py

- Fill in the form with the required property details such as property type, nbr of rooms, etc.
- Click on the "Predict price" button to submit your request. The predicted property price will be displayed.
    
4 . The other way to predict price by using the FastAPI backend which is deployed on render through the below link:

    https://immo-eliza-deployment-1-6o7p.onrender.com/docs
  


```python

```

## ⏱️ Timeline

This project took 5 days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/soha-mohamad-382b44219/).