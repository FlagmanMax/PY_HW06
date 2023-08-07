
#DD.MM.YYYY

month_dict = {31:[1,3,5,7,8,10,12], 30:[4,6,9,11]}

def _leap(year):
    if (year< 1582) or (year % 4 !=0 or year%100 == 0 and year%400 !=0):
        result = False
    else:
        result = True
    return result


def check_date(string_input):
    day, month, year = map(int,string_input.split('.'))
    if 0<day<32 and 0<month<13 and 0<year<10000:
        if month != 2:
            if day in month_dict.keys():
                return month in month_dict[day]
            else:
                return True
        else:
            if _leap(year):
                return day<=29
            else:
                return day<=28
        return True
    else:
        return False


if __name__ == "__main__":
    if check_date(input("Введите дату в формате DD.MM.YYYY: ")):
        print("Дата существует")
    else:
        print("Дата не существует")



