def input_fun():
    print("Время отбытия")
    start = [int(input("Часы: ")), int(input("Минуты: "))]
    print("Время пути")
    travel = [int(input("Часы: ")), int(input("Минуты: "))]
    return start, travel


def count_travel_days(travel):
    return travel[0] // 24


def finish_time(start, travel):
    finishm = travel[1] + start[1]
    finishh = start[0] + travel[0] + finishm // 60
    finishm %= 60
    finishh %= 24
    return finishh, finishm


def output(start, travel):
    print("{} Hours : {} Minutes".format(*finish_time(start, travel)))
    print("{} days".format(count_travel_days(travel)))


output(*input_fun())

