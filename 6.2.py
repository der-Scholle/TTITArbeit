users = [
    {"Login": "user1", "Password": "pass123"},
    {"Login": "user2", "Password": "qwerty"},
    {"Login": "admin", "Password": "admin"},
    {"Login": "test", "Password": "test123"},
    {"Login": "alex", "Password": "alex123"}
]

target_login = "admin"
target_password = "admin"

found = None
for user in users:
    if user["Login"] == target_login and user["Password"] == target_password:
        found = user
        break

if found:
    print("Найден пользователь:", found)
else:
    print("Пользователь не найден")