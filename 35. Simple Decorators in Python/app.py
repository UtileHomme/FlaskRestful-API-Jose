user = {"username": "jose", "access_level": "guest"}


def make_secure(func):
    def secure_function():
        if user["access_level"] == "guest":
            return func()
        else:
            return f"No admin permissions"

    return secure_function


def get_admin_password():
    return "1234"


get_admin_password1 = make_secure(get_admin_password)

print(get_admin_password1)
