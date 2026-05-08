from flask import Flask
from flask_socketio import SocketIO, send
from bb84 import bb84_key
from crypto import encrypt, decrypt

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# FIXED: stable key so encryption/decryption always match
shared_key = bb84_key()

print("Quantum Key (DEBUG):", shared_key)

@socketio.on("message")
def handle_message(msg):
    print("Received:", msg)

    # encrypt then decrypt using SAME key
    encrypted = encrypt(msg, shared_key)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shared_key)
    print("Decrypted:", decrypted)

    send("Server received: " + decrypted)

if __name__ == "__main__":
    socketio.run(app, debug=True)