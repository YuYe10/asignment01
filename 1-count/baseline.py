import time

##############  You can't change here  ##############
addition_times: int = 500_000_000 - 3


def add(num: int) -> int:
    return num + 1


######################################################


if __name__ == "__main__":
    start_time = time.time()
    print("start to calculating...")
    result = 0
    for _ in range(addition_times):
        result = add(result)

    end_time = time.time()
    print(f"Time: {end_time - start_time:.2f}s")
    print(f"Result Is Accepted: {result == addition_times}")
