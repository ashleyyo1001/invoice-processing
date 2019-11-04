import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import credentials
import datetime
import webbrowser
import urllib.request
import ocr
import add
import sp
cred = credentials.Certificate("credentials.json")
#firebase_admin.initialize_app(cred)

# Fetch the service account key JSON file contents
#cred = credentials.Certificate("credentials.json")

# Initialize the app with a service account, granting admin privileges
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'assets-bills.appspot.com',
}, name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("images/2019-10-28 22:50:54.098189.png")

x=(blob.generate_signed_url(datetime.timedelta(seconds=1000), method='GET'))

#webbrowser.open(x)

urllib.request.urlretrieve(x, "firebasetest.jpg")

filename=ocr.image_to_text("test.png")

address=add.get_string(filename) #params: filename

string=ocr.send_string("test.png")

sp.get_details(string)