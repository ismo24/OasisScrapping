import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Access environment variables
API_KEY = os.getenv('API_KEY')



def authenticate(mode):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:{mode}?key={API_KEY}"
    
    payload = {
        "email": "ismaekoura@gmail.com",
        "password": "1234ismo",
        "returnSecureToken": True
    }
    
    response = requests.post(url, json=payload)
    # print(response.json())
    response.raise_for_status()  # Raise an error if the request failed
    
    token = response.json().get('idToken')
    return token

def login():
    token = authenticate('signInWithPassword')
    
    return token

def sign_up():
    token = authenticate('signUp')
    
    return token



# #Firebase allDocumentation
# // Import the functions you need from the SDKs you need
# import { initializeApp } from "firebase/app";
# // TODO: Add SDKs for Firebase products that you want to use
# // https://firebase.google.com/docs/web/setup#available-libraries

# // Your web app's Firebase configuration
# const firebaseConfig = {
#   apiKey: "AIzaSyB80SxC_twH6EWCxfh0iUxj4On6BcWnXEY",
#   authDomain: "oasis-auto-83872.firebaseapp.com",
#   databaseURL: "https://oasis-auto-83872-default-rtdb.europe-west1.firebasedatabase.app",
#   projectId: "oasis-auto-83872",
#   storageBucket: "oasis-auto-83872.appspot.com",
#   messagingSenderId: "986028646652",
#   appId: "1:986028646652:web:0beca7f376ca11b42c3779"
# };

# // Initialize Firebase
# const app = initializeApp(firebaseConfig);


