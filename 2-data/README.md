# 加法计数器

## 目标

1. 从压缩文件 `data.csv.gz` 中读取数据
2. 对数据进行重新计算并保存至 `transformed.csv.gz`

## 动机

1. 如何快速的组织大型数据进行训练

## 帮助链接

1. Ray Data 文档：https://docs.ray.io/en/latest/data/quickstart.html

## 测试

**该部分不需要启动 Docker 环境，你不被允许解压 `data.csv.gz`**

### 读取压缩文件

你应该首先尝试读取数据并打印前 5 条数据进行查看，如果编写正确你会看到如下输出：

```text
{'site_id': 0, 'apple': 194, 'banana': 13, 'orange': 352, 'total_price': 127600}
{'site_id': 1, 'apple': 185, 'banana': 32, 'orange': 238, 'total_price': 96300}
{'site_id': 2, 'apple': 152, 'banana': 30, 'orange': 186, 'total_price': 77000}
{'site_id': 3, 'apple': 184, 'banana': 21, 'orange': 180, 'total_price': 76600}
{'site_id': 4, 'apple': 162, 'banana': 28, 'orange': 206, 'total_price': 83600}
```

数据结构说明如下表所示：

|    site_id    |  apple   |  banana  |  orange  |     total_price      |
| :-----------: | :------: | :------: | :------: | :------------------: |
| 仓库站点的 id | 苹果存量 | 香蕉存量 | 橘子存量 | 所有类别存量的总价值 |

### 对数据进行转换并保存

数据转换需求如下：

1. 由于 `apple` 价值的变化，由原先 100 变为 124.2，所以 `total_price` 需要改变且类型为 `np.float64`。
2. 仓库目前正在考虑进一批新货 `grape`，目前的打算购进的存量是以所有类别中存量最少的一半为基础（向上取整）。

转换完成之后需要保存至 `transformed.csv.gz`，并运行命令 `python test_data.py`。

如果成功将会输出 `Success!`