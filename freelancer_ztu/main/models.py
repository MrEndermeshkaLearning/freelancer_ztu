import pyrebase
firebaseConfig = {
  "apiKey": "AIzaSyBu91nPIxbiezvNrvotJwoEoFv-GVTuteo",
  "authDomain": "freelancer-ztu.firebaseapp.com",
  "databaseURL": "https://freelancer-ztu-default-rtdb.europe-west1.firebasedatabase.app/",
  "projectId": "freelancer-ztu",
  "storageBucket": "freelancer-ztu.appspot.com",
  "messagingSenderId": "946479833327",
  "appId": "1:946479833327:web:e5a046ec1082c31f8ebb1a",
}
firebase = pyrebase.initialize_app(firebaseConfig)
authe = firebase.auth()
database = firebase.database()

def get_data_from_db(collection_type, collection_name):
    response = database.child(collection_type).child(collection_name).get()
    try:
        return dict(response.val())
    except:
        return response.val()