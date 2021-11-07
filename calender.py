year = int(input("Year: "))
month = int(input("Month: "))

def leap_year(year):
    if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# うるう年の判定関数　

def month_day(year,month):
    month_with_30days = [4,6,9,11]
    days = 31
    if month == 2:
        if leap_year(year):
            days = 29
        else:
            days = 28
    elif month in month_with_30days:
        days = 30
    return days
#　該当する月の日数を返す関数

def total_days(year,month):
    total = 0
    for i in range(1900,year):
        if leap_year(i):
            total += 366
        else:
            total += 364
#年ごとにうるう年かどうか判断し、うるう年のときは366、そうでないときは365を足す
    for j in range(1,month):
        total += month_day(year,j)
    return total
#年の日数計算が終わったあと、月の日数を数える　1月から入力された月までの日数なので、rangeは1,monthになり、month_dayを使って月ごとの日数を返し合計する
#1900年から入力された年月の総日数を計算

print("Sun\tMon\tTue\tWed\tThu\tFri\tSat")
week_day = total_days(year,month) % 7 +1
for i in range(week_day % 7):
    print('\t',end = '')
for j in range(1,month_day(year,month) + 1):
    print(j,'\t',end = ''),
    week_day += 1
    if week_day % 7 == 0:
        print('')