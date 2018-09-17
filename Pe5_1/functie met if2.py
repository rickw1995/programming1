def new_password(old, new):
    if new != old and len(new) >=6:
        return True
    else:
        return False

