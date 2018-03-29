import pyrebase
config = {
  "apiKey": "AIzaSyBUTyoqjhDYwPaLXZPg19UnfADPPAG_Nvo",
  "authDomain": "analytical-poet-197513.firebaseapp.com",
  "databaseURL": "https://analytical-poet-197513.firebaseio.com",
  "storageBucket": "analytical-poet-197513.appspot.com",
  "serviceAccount": "C:/Users/nikhi/Downloads/analytical-poet-197513-firebase-adminsdk-n3o8x-29a0434cc4.json"
}
firebase = pyrebase.initialize_app(config)
# Get a reference to the auth service
auth = firebase.auth()
# Log the user in
user = auth.sign_in_with_email_and_password('nefarians123456@gmail.com','jaipur123456')
# Get a reference to the database service
db = firebase.database()
# data to save
data = {
    "name": "Mortimer 'Morty' Smith"
}
# Pass the user's idToken to the push method
results = db.child("users").push(data, user['idToken'])
storage = firebase.storage()
# as admin
storage.child("nefarians/example.jpg").put("example2.jpg")
# as user
storage.child("nefarians/example.jpg").put("example2.jpg", user['idToken'])