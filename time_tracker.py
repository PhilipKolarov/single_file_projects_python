import time


def time_tracker():
    current_time_info = time.localtime()
    h = current_time_info[3]
    m = current_time_info[4]
    s = current_time_info[5]
    while True:
        print(f'{h}:{m}:{s}')
        if s == 59 and m == 59 and h == 23:
            s = 0
            m = 0
            h = 0
        elif s == 59 and m == 59:
            s = 0
            m = 0
            h += 1
        elif s == 59:
            s = 0
            m += 1
        else:
            s += 1
        time.sleep(0.99)


time_tracker()
