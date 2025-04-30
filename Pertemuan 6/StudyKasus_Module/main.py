# M RAVI ACHYAR TRISTA ZHAID
# 1124102193

from auth import login

def main():
    print("=== Program Login Modular ===")
    username = input("Username: ")
    password = input("Password: ")

    if login(username, password):
        print(f"Selamat datang, {username}!")
    else:
        print("Login gagal. Username atau password salah.")

if __name__ == "__main__":
    main()
