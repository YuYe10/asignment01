import time
import ray
##############  You can't change here  ##############
addition_times: int = 500_000_000 - 3

@ray.remote
def add(num: int) -> int:
    return num + 1


######################################################


if __name__ == "__main__":
    print("arranging the worker...")
    ray.init()
    start_time = time.time()
    print("start to calculating...")

    result = 0
    futures = [add.remote(result) for _ in range(addition_times)]
 
    results = ray.get(futures) 
    result = sum(results)
    
    end_time = time.time()
    print(f"Time: {end_time - start_time:.2f}s")
    print(f"Result Is Accepted: {result == addition_times}")
