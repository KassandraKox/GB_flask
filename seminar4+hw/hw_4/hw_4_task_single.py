import time

res = 0


def sum_list(lst):
    global res
    for i in lst:
        res += i


def task(sep_list):
    start_time = time.time()
    for sep in sep_list:
        sum_list(sep)

    return res, time.time() - start_time