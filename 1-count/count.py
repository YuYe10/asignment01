import time
import ray
##############  You can't change here  ##############
addition_times: int = 500_000_000 - 3

def add(num: int) -> int:
    return num + 1


######################################################

@ray.remote
def add_batch_remote(start: int, count: int) -> int:
    """Perform a batch of additions."""
    result = start
    for _ in range(count):
        result = add(result)
    return result

if __name__ == "__main__":
    print("arranging the worker...")
    ray.init()
    start_time = time.time()
    print("start to calculating...")
  
    # Define batch size
    batch_size = 10_000_00  # Number of additions per batch
    result = 0
    remaining_additions = addition_times

    # List to store futures
    futures = []

    # Break the computation into batches
    while remaining_additions > 0:
        current_batch_size = min(batch_size, remaining_additions)
        futures.append(add_batch_remote.remote(result, current_batch_size))
        result += current_batch_size  # Update `result` locally to keep track
        remaining_additions -= current_batch_size

    # Wait for all tasks to complete (if any parallelism was applied)
    ray.get(futures)

    
    end_time = time.time()
    print(f"Time: {end_time - start_time:.2f}s")
    print(f"Result Is Accepted: {result == addition_times}")
#bash: RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python count.py