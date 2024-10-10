import time

##############  You can't change here  ##############
addition_times: int = 500_000_000 - 3


def add(num: int) -> int:
    return num + 1


######################################################


if __name__ == "__main__":
    print("arranging the worker...")

    start_time = time.time()
    print("start to calculating...")

    result = -1

    end_time = time.time()
    print(f"Time: {end_time - start_time:.2f}s")
    print(f"Result Is Accepted: {result == addition_times}")
