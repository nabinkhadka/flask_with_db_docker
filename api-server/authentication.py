from functools import wraps
from flask import request, abort
import jwt
import os

JWT_SECRET = os.getenv("JWT_SECRET")


def authorize(f):
    @wraps(f)
    def decorated_function(*args, **kws):
        data = request.json
        username = data.get("name")
        if username != "tapai_ko_name":
            abort(403)
        return f(*args, **kws)
    return decorated_function
