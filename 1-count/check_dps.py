import os
import time
import socket
from collections import Counter

import ray
from dotenv import load_dotenv


# Step2: Define the remote `get_host` function
@ray.remote  
def get_host():    
    ip_address = socket.gethostbyname(socket.gethostname()) 
    return ip_address  


if __name__ == "__main__":

    load_dotenv(dotenv_path="../.env")

    client_port = os.getenv("CLIENT_PORT")

    # Step1: Connect to the Ray cluster
    ray.init(address="auto")
    # Step3: Generate a list with 100 `get_host` tasks
    num_tasks = 100  
    tasks = [get_host.remote() for _ in range(num_tasks)]
    # Step4: Get the IP addresses of the machines that executed the tasks
    ip_addresses = ray.get(tasks)
    """ print(tasks)
    print("\n")
    print(ip_addresses) """
    print("Tasks executed")
    for ip_address, num_tasks in Counter(ip_addresses).items():
        print(f"    {ip_address} tasks on {num_tasks}")
#bash: RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python count.py