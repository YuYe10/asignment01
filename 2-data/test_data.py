import ray.data
import numpy as np
from pyarrow import float64, int64

ds = ray.data.read_csv("output.csv.gz", arrow_open_stream_args={"compression": "gzip"})

cols = ["apple", "banana", "orange", "total_price", "grape", "site_id"]


for name, type in zip(ds.schema().names, ds.schema().types):
    assert name in cols
    if name == "total_price":
        assert type == float64()
    else:
        assert type == int64()

for row in ds.iter_rows():
    total_price = row["total_price"]
    apple = row["apple"]
    banana = row["banana"]
    orange = row["orange"]
    grape = row["grape"]

    target_total_price = apple * 124.2 + banana * 200 + orange * 300
    target_grape = np.ceil(np.min([apple, banana, orange]) / 2).astype(int)
    assert np.isclose(target_total_price, total_price), f"{total_price}, {target_total_price}"
    assert target_grape == grape, f"{grape}"

print("Success!")
