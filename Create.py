from firebase import firebase

firebase = firebase.FirebaseApplication("https://python-firebase-63d55.firebaseio.com/", None)
data = {
    'Nama':'Ilham Gumantung Gusti',
    'Email':'iggusti@gmail.com',
    'HP':82126258198
}

result = firebase.post('/Customer/', data)
print(result)