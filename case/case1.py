
def kaka_map():
    n = 5
    al = [9, 20, 28, 18, 11]
    bl = [30, 1, 21, 17, 28]
    rl = []
    for idx, a in enumerate(al):
        x = "{0:b}".format(al[idx]).zfill(n)
        y = "{0:b}".format(bl[idx]).zfill(n)
        print(x, y)
        b = bin(int(x, 2) | int(y, 2))[2:]
        rr = b.replace("1", "#")
        rl.append(rr)
    print(rl)


def kaka_dart(in_str):
    result = []
    point = None
    point_list = ["0","1","2","3","4","5","6","7","8","9"]
    bonus_list = ["S","D","T"]

    for c in in_str:
        if point == 1 and c == "0":
            point = 10
        elif point is None and c in point_list:
            point = point_list.index(c)
        elif point is not None and c in point_list:
            result.append(point)
            point = point_list.index(c)
        elif c in bonus_list:
            point = point ** (bonus_list.index(c) + 1)
        elif c == "*":
            point = point * 2
            result.append(point)
            if len(result) > 1:
                result[len(result) - 2] = result[len(result) - 2] * 2
            point = None
        elif c == "#":
            point = point * -1
            result.append(point)
            point = None

    if point is not None:
        result.append(point)

    print(sum(result))


def kaka_cache(c_size, citys):
    cache = []
    cal_time = 0
    for c in citys:
        c = c.lower()
        if c in cache:
            cal_time += 1
        else:
            if 0 < c_size <= len(cache):
                cache.pop(0)
            cache.append(c)
            cal_time += 5

    print(cal_time)


def kaka_bus(n, t, m, timetable):
    print("start----")
    rl = list(int(time.split(":")[0])*60 + int(time.split(":")[1]) for time in timetable)
    rl.sort()
    print(rl)
    last_bus_c = 0
    last_ride_time = 0
    for num in range(0, n):
        now = 540 + num * t
        pop_count = 0
        tmp_rl = rl.copy()
        last_bus_c = 0
        for r in rl:
            if r <= now and pop_count < m:
                tmp_rl.pop(tmp_rl.index(r))
                pop_count += 1
                # print("pop:", r)
                last_bus_c += 1
                last_ride_time = r
        rl = tmp_rl
        # print("remain:", rl)

    if last_bus_c < m:  # can ride.
        # print("Remain!!", m - last_bus_c)
        last_min = 540 + (n-1) * t
    else:
        last_min = last_ride_time - 1
        # print("Full!!")

    print("--Result: {0:02n}:{1:02n}".format(int(last_min / 60), last_min % 60))


def jaccard(left, right):
    left = left.lower()
    right = right.lower()

    left_pairs = _pair_list(left)
    right_pairs = _pair_list(right)
    print("{},{}".format(left_pairs, right_pairs))
    n_count = 0
    u_count = 0
    for l in left_pairs:
        if l in right_pairs:
            n_count += 1
    u_count = len(left_pairs + right_pairs) - n_count
    print("{},{}".format(n_count, u_count))
    if u_count == 0:
        jn = 1
    else:
        jn = n_count / u_count
    print("Result:", int(jn * 65536))


def _pair_list(s):
    pairs = []
    for l in range(0, len(s) - 1):
        pair = s[l] + s[l + 1]
        if pair.isalpha() is False:
            continue
        pairs.append(pair)
    return pairs