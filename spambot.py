from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

CLIENT_SECRET_FILE = 'client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#for i in range(1, 1000):
    # recepient = 'percapitaoutcome@gmail.com'
#    conv = str(i)
    # while (len(conv) < 4):
    #     conv = '0' + conv
    # recepient = 'f2020' + conv + '@hyderabad.bits-pilani.ac.in'
mimeMessage = MIMEMultipart()
mimeMessage['subject'] = 'Testing'
emailMsg = 'Consider yourself fortunate for being selected for testing of automated send scripts'
mimeMessage['to'] = 'percapitaoutcome@gmail.com'
mimeMessage.attach(MIMEText(emailMsg, 'plain'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()
message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)

print('Spam completed successfully')
