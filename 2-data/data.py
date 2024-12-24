import ray
import numpy as np
import pandas as pd 
from numpy.typing import NDArray

# Complete the function
def transform(batch: dict[str, NDArray]) -> dict[str, NDArray]:

    batch['total_price'] = batch['total_price'].astype(np.float64) + batch['apple'].astype(np.float64)*(124.2-100.0)

    columns_indices = ['apple', 'banana', 'orange']  

    batch_array = np.array([batch[col] for col in columns_indices]) 
    # print("处理的 batch_array 内容:", batch_array)

    min_value = np.min(batch_array, axis=0)
    # print("处理的 min_value 内容:", min_value)
    
    batch['grape'] = np.ceil(min_value / 2).astype(int)
    # print("处理的 batch['grape'] 内容:", batch['grape'])

    return batch 

if __name__ == "__main__":

    # 读取压缩文件 data.csv.gz
    ds = ray.data.read_csv("data.csv.gz", arrow_open_stream_args={"compression": "gzip"})
    print(ds.materialize())
    ds.show(limit=5)

    transformed_ds = ds.map_batches(transform)
    print(transformed_ds.materialize())

    # 将字典数据转换为 DataFrame  
    df = transformed_ds.to_pandas()  

    # 保存为压缩的 CSV  
    df.to_csv('transformed.csv.gz', index=False, compression='gzip')

