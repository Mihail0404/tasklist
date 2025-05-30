import hashlib

def get_hash(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()