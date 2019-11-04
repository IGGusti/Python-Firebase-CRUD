from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-firebase-63d55.firebaseio.com/", None)

result = firebase.get('/Customer', '')
print(result)