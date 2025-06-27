tasks = [
    {"DateStart": "2025-06-01", "DateFinish": "2025-06-05", "Description": "Учеба"},
    {"DateStart": "2025-06-02", "DateFinish": "2025-06-10", "Description": "Работа"},
    {"DateStart": "2025-06-03", "DateFinish": "2025-06-08", "Description": "Спорт"},
    {"DateStart": "2025-06-04", "DateFinish": "2025-06-10", "Description": "Отдых"},
    {"DateStart": "2025-06-05", "DateFinish": "2025-06-07", "Description": "Путешествие"}
]

latest = tasks[0]
for task in tasks:
    if task["DateFinish"] > latest["DateFinish"]:
        latest = task

print("Самое позднее занятие:", latest["Description"], "до", latest["DateFinish"])