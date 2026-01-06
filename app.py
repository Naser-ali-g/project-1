from flask import Flask, jsonify
import os

app = Flask(__name__)
PORT = int(os.environ.get('PORT', 5000))

@app.route('/')
def hello_world():
    return ' Big hello from Nasro to Meno (Mennallah saber) my best Friend ever no ci !'

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)