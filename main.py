from flask import Flask, jsonify
from routes.user_route import user_route

app = Flask(__name__)

app.register_blueprint(user_route)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)