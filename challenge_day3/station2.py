import datetime

def solution_station_2(string):
    date = datetime.datetime.strptime(string, '%Y-%m-%d')
    day_num = date.weekday()

    days = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]

    return str(days[day_num])