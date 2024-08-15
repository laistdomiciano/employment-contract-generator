from flask import request

def validate_signup(data):
    # Simple validation example
    if not data['name'] or not data['email'] or not data['username']:
        return "Missing required fields"
    if data['password1'] != data['password2']:
        return "Passwords do not match"
    return None

