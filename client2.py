
import requests

SERVER_URL = 'http://127.0.0.1:5000'

def send_message(username, message):
    response = requests.post(f'{SERVER_URL}/send', json={'username': username, 'message': message})
    print(response.json())

def get_messages():
    response = requests.get(f'{SERVER_URL}/messages')
    for msg in response.json():
        print(f"{msg['username']}: {msg['message']}")

if __name__ == '__main__':
    send_message('Client2', 'Hello from Client 2!')
    get_messages()
