class RecentCounter:

    def __init__(self):
        self.records = []
        self.start = 0
    def ping(self, t: int) -> int:
        self.records.append(t)
        while self.records[self.start] < t - 3000:
            self.start += 1

        return len(self.records) - self.start


if __name__ == "__main__":
    rc = RecentCounter()

    print(rc.ping(1))     # expected 1
    print(rc.ping(100))   # expected 2
    print(rc.ping(3001))  # expected 3
    print(rc.ping(3002))  # expected 3