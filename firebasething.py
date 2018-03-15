from firebase import firebase
firebase = firebase.FirebaseApplication('https://nefarians-8bf36.firebaseio.com/', None)
result = firebase.get('/users',None)
print(result)