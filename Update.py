from firebase import firebase

firebase = firebase.FirebaseApplication('https://python-firebase-63d55.firebaseio.com/', None)
firebase.put('/Customer/-LsoJ8vdcTRd-oTTwOi2/','Nama','Gugum')
result = firebase.get('/Customer', '')
print('Record -LsoJ8vdcTRd-oTTwOi2 Updated')
print(result)