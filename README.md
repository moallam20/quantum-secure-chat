#  Quantum Secure Chat (BB84 Simulation)

##  Overview

This project is a **quantum-inspired secure messaging system** that simulates the BB84 Quantum Key Distribution (QKD) protocol. The generated shared secret key is used to encrypt and decrypt real-time chat messages using AES encryption.

The goal is to demonstrate how **future quantum-safe communication systems** can be designed using quantum cryptography principles.

---

##  Problem Statement

Traditional encryption systems such as RSA and AES rely on mathematical complexity. However, future quantum computers may be able to break some classical encryption methods.

This project explores a **quantum-inspired alternative approach** using BB84-based key generation to enhance secure communication concepts.

---

##  Solution

The system works as follows:

1. Simulates BB84 quantum key distribution
2. Generates a shared secret key between sender and receiver
3. Uses AES encryption to secure messages
4. Provides real-time chat communication using WebSockets

---

##  Key Features

- BB84 quantum key distribution simulation
- Secure AES encryption & decryption
- Real-time chat system using Flask and Socket.IO
- Basic eavesdropping detection concept (error simulation)
- Simple web-based user interface (HTML + JavaScript)

---

##  Technologies Used

- Python
- Flask
- Flask-SocketIO
- HTML
- JavaScript
- Cryptography (AES)



## 🏗️ Project Structure

