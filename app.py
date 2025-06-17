from flask import Flask, render_template, request, redirect, url_for, session
from crypto_utils import generate_keys, derive_shared_key, encrypt_message, decrypt_message
from auth_utils import generate_otp, send_otp_email, validate_otp
import sqlite3
import base64  # For encoding nonce

app = Flask(__name__)
app.secret_key = "your_super_secret_key"
