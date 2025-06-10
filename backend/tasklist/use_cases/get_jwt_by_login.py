import jwt
import os

SECRET_KEY = "89329802398a"

ALGORITM = "HS256"

def get_encoded_user(userid, login, name):
    encoded_userdata = jwt.encode({"id": userid, "login": login, "name": name}, SECRET_KEY, ALGORITM)
    return encoded_userdata

def get_decoded_userdata_by_jwt(token):
    decoded_userdata = jwt.decode(token, SECRET_KEY, ALGORITM)
    return decoded_userdata