# immo-eliza-deployment 🏠
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white)


## 🏢 Description
This project aims to deploy a machine learning model to predict property prices through an API endpoint. It also includes a streamlit web application for easier interaction with the model. The project is structured into two main parts: 
 - The API for developers 
 - User-friendly web application for non-technical users. 

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

- The FastAPI backend is deployed on Render, containerized with Docker.
- The Streamlit web page hosted with Streamlit Community Cloud.
<br>

## 🛎️ Usage

- **Local app:**

    - Clone the repository to your local machine.

        https://github.com/soha-ms/immo-eliza-deployment.git

    - Navigate to the project directory and install the required dependencies:

        pip install -r requirements.txt

    - Open command prompt on *api* directory and run below command:

            uvicorn app:app --reload

    - Navigate to the project *streamlit* directory and run below command:      

            streamlit run streamlit.py

- **FastAPI :**

    Open your web browser and try out post predict on [FastAPI app's URL deployed on Render](https://immo-eliza-deployment-1-6o7p.onrender.com/docs).

        - Fill in the json with the required property details.
        - Click on the "Execute" button to submit your request to see the returnd json prediction. 

- **Streamlit App:**

    Open your web browser and navigate to the [Streamlit app's URL hosted with  Streamlit](https://immo-eliza-deployment-pevp8uygv7w9vdxezzjwbh.streamlit.app/).

        - Fill in the form with the required property details such as property type, nbr of rooms, etc.
        - Click on the "Predict price" button to submit your request. The predicted property price will be displayed.    


## ⏱️ Timeline

This project took 5 days for completion.

<br>

## 🔧 To be upgraded
- **Add range values hints for Energy consumption fields**: 
- **Test Model/others to enhance prediction and add extra fileds such as epc, locality**: 
<br>

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 

Connect with me on [LinkedIn](https://www.linkedin.com/in/soha-mohamad-382b44219/).