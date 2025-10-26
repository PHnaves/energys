logged_user = None

def set_logged_user(user_data):
    global logged_user
    logged_user = user_data

def get_logged_user():
    return logged_user

def clear_session():
    global logged_user
    logged_user = None
