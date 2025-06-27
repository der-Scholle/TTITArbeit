sessions = [
    {"code": "C001", "year": 2025, "month": 1, "duration": 45},
    {"code": "C002", "year": 2025, "month": 2, "duration": 90},
    {"code": "C003", "year": 2025, "month": 3, "duration": 30},
    {"code": "C004", "year": 2025, "month": 4, "duration": 60},
    {"code": "C005", "year": 2025, "month": 5, "duration": 120}
]

longest = shortest = sessions[0]

for session in sessions:
    if session["duration"] > longest["duration"]:
        longest = session
    if session["duration"] < shortest["duration"]:
        shortest = session

print("Самое долгое занятие:", longest["code"], longest["duration"], "мин")
print("Самое короткое занятие:", shortest["code"], shortest["duration"], "мин")