import time
import ray
##############  You can't change here  ##############
addition_times: int = 500_000_000 - 3


def add(num: int) -> int:
    return num + 1


######################################################
'''Reference from GPT-4o'''


@ray.remote(num_cpus=2)
def add_batch(num: int, batch_size: int) -> int:
    result = num
    for _ in range(batch_size):
        result = add(result)
    return result


'''Reference from GPT-4o'''
if __name__ == "__main__":
    print("arranging the worker...")
    ray.init()
    num_time = time.time()
    print("start to calculating...")
    '''Reference from GPT-4o'''
    # 定义一轮要执行的任务数
    batch_size = 10_000_00
    result = 0
    remaining_additions = addition_times

    # 创建futures列表
    futures = []

    while remaining_additions > 0:
        # 由于 addition_times 不一定是 batch_size 的倍数，最后一批可能会小于 batch_size，因此在每次循环中动态调整 current_size
        current_size = min(batch_size, remaining_additions)
        futures.append(add_batch.remote(result, current_size))
        result += current_size  # Update `result` locally to keep track
        remaining_additions -= current_size

    #等待所有任务完成
    ray.get(futures)

    '''Reference from GPT-4o'''

    end_time = time.time()
    print(f"Time: {end_time - num_time:.2f}s")
    print(f"Result Is Accepted: {result == addition_times}")
# bash: RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python count.py
