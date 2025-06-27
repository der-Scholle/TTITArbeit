sessions = [
    {"code": "C001", "year": 2022, "month": 1, "duration": 45},
    {"code": "C002", "year": 2022, "month": 2, "duration": 60},
    {"code": "C003", "year": 2023, "month": 3, "duration": 90},
    {"code": "C004", "year": 2023, "month": 4, "duration": 120},
    {"code": "C005", "year": 2023, "month": 5, "duration": 45},
    {"code": "C006", "year": 2024, "month": 1, "duration": 60},
    {"code": "C007", "year": 2024, "month": 2, "duration": 75},
    {"code": "C008", "year": 2024, "month": 3, "duration": 90},
    {"code": "C009", "year": 2024, "month": 4, "duration": 30},
    {"code": "C010", "year": 2024, "month": 5, "duration": 45}
]

year_total = {}

for session in sessions:
    if session["year"] in year_total:
        year_total[session["year"]] += session["duration"]
    else:
        year_total[session["year"]] = session["duration"]

max_year = min(year_total.keys())
max_duration = year_total[max_year]

for year, duration in year_total.items():
    if duration > max_duration or (duration == max_duration and year < max_year):
        max_year = year
        max_duration = duration

print("Год с наибольшей продолжительностью:", max_year)
print("Суммарная продолжительность:", max_duration, "мин")