def accum(s):
    return "-".join(list(c.upper() + c.lower() * n for n, c in enumerate(s)))


def change_w(s):
    return "".join(list(c.upper() if c == "w" else c for c in s))


class Calculator:
    a = [1, 2, 3, 4]

    def __init__(self):
        self.result = 0

    def __len__(self):
        return len(self.a)

    def add(self, num):
        self.result += num
        return self.result

    def len(self):
        return len(self.a)


if __name__ == "__main__":
    print(change_w("Hello world!"))

    print(accum("test!!"))

    cal = Calculator()
    cal.add(4)
    print(dir(cal))
    print(len(cal))
    cal.len()
    print(("test".__len__()))
