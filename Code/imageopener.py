import pyrebase
from PIL import Image
import urllib.request

config = {
  "apiKey":"AIzaSyBUTyoqjhDYwPaLXZPg19UnfADPPAG_Nvo",
  "authDomain":"analytical-poet-197513.firebaseapp.com",
  "databaseURL":"https://analytical-poet-197513.firebaseio.com",
  "storageBucket":"analytical-poet-197513.appspot.com",
  "serviceAccount":"C:/Users/foxfi/Downloads/analytical-poet-197513-firebase-adminsdk-n3o8x-e8b8734737.json"
}
firebase = pyrebase.initialize_app(config)

auth = firebase.auth()

# Log the user in
user = auth.sign_in_with_email_and_password("nefarians123456@gmail.com", "jaipur123456")

# Get a reference to the database service
db = firebase.database()

users = db.child(" Elizabeth II").get()


URL = users.val()

with urllib.request.urlopen(URL) as url:
    with open('temp.jpg', 'wb') as f:
        f.write(url.read())

img = Image.open('temp.jpg')

img.show()


