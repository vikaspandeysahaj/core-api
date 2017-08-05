import hashlib
from functools import wraps

from flask import request,  abort, g

from api.models.user import User


def authenticate(f):
    @wraps(f)
    def extract_token(*args, **kwargs):
            user_email = request.headers.get("EMAIL")
            if user_email:
                user = User.find_by_email(user_email)
                if not user:
                    return abort(401)
                else:
                    g.current_user = user
                    return f(*args, **kwargs)

            else:
                return abort(401)

    return extract_token
