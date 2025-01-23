
from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista przechowująca wiadomości
messages = []

@app.route('/send', methods=['POST'])
def send_message():
    data = request.json
    if 'username' in data and 'message' in data:
        messages.append({'username': data['username'], 'message': data['message']})
        return jsonify({'status': 'Message received'}), 200
    return jsonify({'error': 'Invalid data'}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    return jsonify(messages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
