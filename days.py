def day_number(date):
    month_days = [31, 28, 31, 30, 31, 30,
                  31, 31, 30, 31, 30, 31]
    month, day = map(int, date.split("-"))
    return sum(month_days[:month - 1]) + day


def count_days_together(arriveAlice, leaveAlice, arriveBob, leaveBob):
    start = max(day_number(arriveAlice), day_number(arriveBob))
    end = min(day_number(leaveAlice), day_number(leaveBob))
    return max(0, end - start + 1)


print(count_days_together("08-15", "08-18", "08-16", "08-19"))
