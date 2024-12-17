# 学习体会
## 1-count
### 一、完成check_dps.py

1.提交job到ray cluster

一直没找到如何从脚本中访问启动在docker容器, 就直接把脚本通过Job Server提交到ray集群中运行了(不过还有一个NoneType错误不知道怎么搞~~~)
参考文章:[Ray 单机部署&多机部署&docker部署](https://blog.csdn.net/m0_62162986/article/details/131316894)
~~~bash
RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python <name_of_script>.py
~~~

2.完成count.py

如果直接执行并行化处理会导致内存不足而杀死进程, 这也违背了并行化处理加快处理的目的(把add函数加上remote装饰器也违背了考核要求):
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

定义打包计算函数add_batch():
~~~python
@ray.remote
def add_batch(num: int, batch_size: int) -> int:
    result = num
    for _ in range(batch_size):
        result = add(result)
    return result
~~~