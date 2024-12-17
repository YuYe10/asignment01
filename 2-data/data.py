import ray
import numpy as np
from numpy.typing import NDArray


# Complete the function
def transform(batch: dict[str, np.ndarray]) -> dict[str, np.ndarray]:
    # 更新 `total_price`，苹果的单价从 100 调整到 124.2
    new_total_price = (
        batch["apple"] * 124.2 + batch["banana"] * 100 + batch["orange"] * 150
    ).astype(np.float64)
    
    # 计算 grape 的存量：所有类别中存量最少的一半（向上取整）
    min_stock = np.minimum.reduce([batch["apple"], batch["banana"], batch["orange"]])
    grape_stock = np.ceil(min_stock / 2).astype(np.int64)

    # 返回更新后的数据
    return {
        "site_id": batch["site_id"],
        "apple": batch["apple"],
        "banana": batch["banana"],
        "orange": batch["orange"],
        "grape": grape_stock,
        "total_price": new_total_price,
    }


if __name__ == "__main__":
    # 初始化 Ray
    ray.init()

    # 读取压缩文件 data.csv.gz
    ds = ray.data.read_csv("data.csv.gz", arrow_open_stream_args={"compression": "gzip"})

    # 打印前 5 条数据
    print("First 5 rows of the dataset:")
    print(ds.take(5))
    '''
    Example Output:
        {'site_id': 0, 'apple': 194, 'banana': 13, 'orange': 352, 'total_price': 127600}
        {'site_id': 1, 'apple': 185, 'banana': 32, 'orange': 238, 'total_price': 96300}
        {'site_id': 2, 'apple': 152, 'banana': 30, 'orange': 186, 'total_price': 77000}
        {'site_id': 3, 'apple': 184, 'banana': 21, 'orange': 180, 'total_price': 76600}
        {'site_id': 4, 'apple': 162, 'banana': 28, 'orange': 206, 'total_price': 83600}
    '''

    """ # 转换数据
    transformed_ds = ds.map_batches(transform)

    # 保存结果至 transformed.csv.gz
    transformed_ds.write_csv("transformed.csv.gz")

    # 关闭 Ray
    ray.shutdown() """
