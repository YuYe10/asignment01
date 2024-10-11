import os
import time
import socket
from collections import Counter

import ray
from dotenv import load_dotenv


# Step2: Define the remote `get_host` function
@ray.remote
def get_host():
    time.sleep(0.001)
    return socket.gethostbyname(socket.gethostname())


if __name__ == "__main__":

    load_dotenv(dotenv_path="../.env")

    client_port = os.getenv("CLIENT_PORT")

    # Step1: Connect to the Ray cluster
    ray.init(address=f"auto", _temp_dir=None, ignore_reinit_error=True)
    # Step3: Generate a list with 100 `get_host` tasks
    tasks = [get_host.remote() for _ in range(100)]
    # Step4: Get the IP addresses of the machines that executed the tasks
    ip_addresses = ray.get(tasks)

    print("Tasks executed")
    for ip_address, num_tasks in Counter(ip_addresses).items():
        print(f"    {ip_address} tasks on {num_tasks}")
