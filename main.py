import random

with open("data.csv", "w") as f:
    f.write("site_id,apple,banana,orange,total_price\n")
    for i in range(100):
        site_id = i
        apple = random.randint(50, 200)
        banana = random.randint(10, 50)
        orange = random.randint(100, 400)
        total_price = apple * 100 + banana * 200 + orange * 300
        f.write(f"{site_id},{apple},{banana},{orange},{total_price}\n")
