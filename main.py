import os
import pickle
import base64
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
import pyperclip
import re

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def authenticate():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return creds


def get_last_email_content():
    global text
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)
    results = service.users().messages().list(userId='me', labelIds=['INBOX'], maxResults=1).execute()
    messages = results.get('messages', [])
    if not messages:
        print('No unread messages found.')
        return None
    message = messages[0]
    msg = service.users().messages().get(userId='me', id=message['id']).execute()
    payload = msg['payload']
    headers = payload['headers']
    for header in headers:
        if header['name'] == 'Subject':
            subject = header['value']
    body = payload['body']
    if 'data' in body:
        data = body['data']
        text = base64.urlsafe_b64decode(data).decode('utf-8')
    else:
        parts = payload.get('parts')
        if parts:
            for part in parts:
                mimeType = part['mimeType']
                if mimeType == 'text/plain':
                    data = part['body']['data']
                    text = base64.urlsafe_b64decode(data).decode('utf-8')
                    break
    return subject, text


email_content = get_last_email_content()

if email_content:
    subject, text = email_content
    verifiedSubject = subject
    verifiedText = text


def filter_numbers(text):
    pattern = r'\d+'
    numbers = re.findall(pattern, text)
    filtered_text = ''.join(numbers)
    return filtered_text


authCode = filter_numbers(verifiedText)
pyperclip.copy(authCode)
