<center><h1>AI 考核二<br/>任务 1</h1></center>

## 诚信声明

_注：做此该声明是希望能通过第三方约束辅助你进行学习。_

在每个任务中你可以使用任何工具辅助你完成该任务，但你 **不被允许直接复制与抄写**，若你借用了如 GPT、CSDN、GitHub 等提供的方案代码或解决办法，请你需要 **在该代码段起始与结束标记来源**，以下是一个例子：

```python
def foo():
  # start: copy from [GPT|url]
  pass # code brick
	# end: copy from [GPT|url]
```

每次提交任务都会有相应的检查，一经发现则 ==**立即失去考核资格**==。

## 任务 1

_在接下来的 `assignment01` 和 `assignment02` 都十分容易，其目的性是为了解原理和学习提高运行速度的思想_

- 数据并行，是指将数据拆分为若干块并分配给工作节点处理的模式。
- 张量并行，是指将模型的权重矩阵或其他相关的数据结构被划分成多个小块，每一块由不同的处理器独立处理的模式。

具体选择策略为：如果单张 GPU 可以放入模型则优先选择数据并行，除非所处理的任务不满足可以拆分的条件；否则选择张量并行。

张量并行将需要考虑相当的通信效率，因为模型的权重矩阵是彼此依赖的，其需要在上一个处理器中完成数据运算再传递下一个处理器中，所以这显然没有数据并行效率来得高，因为一旦分配完毕数据，各工作节点只需要运算自己分配到的工作并向 master 节点反馈即可。

所以在本次任务之下，我们将利用 Ray （分布式框架）完成数据并行的模拟，具体任务如下：

1. 利用 Ray 做一个简单的加法计数
2. 利用 Ray 读取文件创建数据中心
3. 阅读 Ray-ML 的部分（Optional）
4. 整理你的工作并发送至相应的邮箱。

相应的要求请查看具体目录下的 `README.md` 文件

本次任务的环境如下：

- Python 3.10
- 基础软件包可以利用 `pip install -r requirements.txt` 安装
- docker 和 docker-compose v2

## 3 整理文件

你必须以 **正确** 的格式提交内容，否则视为 **无效提交**，格式如下：

```text
.
└── 1-count
    └── count.py
    └── score.txt
    └── note.md
    2-data
    └── data.py
    3-ml # 如果你想与我们分享你的阅读结果或一些完成的项目（不易太大，例如超过 30 MB）
```

请以压缩包的形式发送给指定的地址（请关注具体的消息）并以你的 `年纪 _姓名` 命名，如 `23级_张三`。
