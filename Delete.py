from firebase import firebase

firebase = firebase.FirebaseApplication('https://python-firebase-63d55.firebaseio.com/', None)
firebase.delete('/Customer/','-LsoJ9kpjYa4wvTExkJT')
result = firebase.get('/Customer', '')
print('Record -LsoJ8vdcTRd-oTTwOi2 Deleted')
print(result)