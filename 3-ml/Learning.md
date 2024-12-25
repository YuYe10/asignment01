# 学习历程

## 1-count

### 一、完成check_dps.py

#### 提交job到ray cluster

一直没找到如何从脚本中访问启动在docker容器中的ray集群, 就直接把脚本通过bash命令提交到ray集群中运行了  
参考文章:[Ray 单机部署&多机部署&docker部署](https://blog.csdn.net/m0_62162986/article/details/131316894)

~~~bash
RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python <name_of_script>.py
~~~

### 二、完成count.py

如果直接执行并行化处理会导致[内存不足而杀死进程](https://docs.ray.io/en/latest/ray-core/patterns/ray-get-too-many-objects.html)，这也违背了[并行计算加快速度](https://docs.ray.io/en/latest/ray-core/patterns/ray-get-loop.html)的目的  
(把add函数加上remote装饰器也违背了考核要求)  
ray.get()的用法:[ray.get](https://docs.ray.io/en/latest/ray-core/api/doc/ray.get.html)

~~~python
    @ray.remote
    def add(num: int) -> int:
        return num + 1

    result = 0
    futures = [add.remote(result) for _ in range(addition_times)]
 
    results = ray.get(futures) 
    result = sum(results)
~~~

所以之后我采用打包处理以降低内存消耗:  
定义批计算函数add_batch():

~~~python
@ray.remote
def add_batch(num: int, batch_size: int) -> int:
    result_i = num
    for _ in range(batch_size):
        result_i = add(result)
    return result_i
~~~

这样能够减少内存占用，防止进程终止，使用本地的add()函数也能加快运算速度

主体代码如下：

~~~python
    while remaining_additions > 0:
        # 由于 addition_times 不一定是 batch_size 的倍数，最后一批可能会小于 batch_size，因此在每次循环中动态调整 current_size
        current_size = min(batch_size, remaining_additions)
        futures.append(add_batch.remote(result, current_size))
        result += current_size  # 更新本地result以保证结果被接受
        remaining_additions -= current_size

    # 等待所有任务完成执行ray.get()(阻塞)
    ray.get(futures)
~~~

## 2-data
### 完成data.py

主要使用numpy里的工具对数据进行处理，主要注意最后要把数据集从Dataset转为pandas的DataFrame再储存为'transformed.csv.gz'  
不然会出现zlib解压的[OSError](https://geek-docs.com/python/python-ask-answer/354_python_zliberror_error_3_while_decompressing_incorrect_header_check.html):

~~~python
    # 对读取的数据集进行转换
    transformed_ds = ds.map_batches(transform)
    # print(transformed_ds.materialize())

    # 将字典数据转换为 DataFrame  
    df = transformed_ds.to_pandas()  

    # 保存为压缩的 CSV  
    df.to_csv('transformed.csv.gz', index=False, compression='gzip')
~~~