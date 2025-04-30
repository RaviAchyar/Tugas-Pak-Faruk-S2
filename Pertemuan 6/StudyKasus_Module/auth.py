# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

def login(username, password):
    users = {
        "admin": "1234",
        "user": "abcd"
    }

    if username in users and users[username] == password:
        return True
    return False
