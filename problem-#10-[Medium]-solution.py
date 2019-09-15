import time, datetime


def basic_funct():
    print(f"{datetime.datetime.now().replace(microsecond=0)} - Calling function...")


def scheduler(f, n):  # calls f after n milliseconds
    time.sleep(n / 1000)  # convert seconds to milliseconds
    f()


if __name__ == "__main__":
    while True:
        scheduler(basic_funct, 5000)

