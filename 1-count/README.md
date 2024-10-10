# 加法计数器

## 目标

1. 利用 `ray.remote` 构造一个可以分布式运行的函数
2. 将 `baseline.py` 中的数据进行合理的分发以变更为并行结构
3. 调节 `.env` 中的 `NUM_WORKERS` 和 `NUM_CPU_WORKER` 字段的值，查看不同核心数下和不同模拟的节点数下，采取相同的分发策略有什么不同（Optional）

## 动机

1. 此任务是为了熟悉如何利用 Ray 高效的搭建分布式程序完成数据并行
2. 理解应该如何分发数据的数量和具体算力之间的关系

## 帮助链接

1. Ray 文档：https://docs.ray.io/en/latest/ray-overview/getting-started.html

## 测试

### 分布式运行函数

首先你应该优先完成 `check_dps.py` 的内容，来帮助你熟悉 Ray 中提供的几个重要的原语

**你不被允许修改除有 Step 标记的部分**

你需要了解 `ray.remote` 中的一些参数，可以帮助你快速指定运行一个分布式函数/类需要分配多少资源，这个操作十分关键的，可以极大的提供运行效率，你可以在之后的完成的 `count.py` 中测试指定资源与不指定资源的性能差距。

在你完成 `check_dps.py` 之前，你应该先将 `.env.example` 复制一份并将拷贝的改名为 `.env`。若你的平台资源不够分配如此多的 CPU 你应该降低一些参数；若你的平台是 Apple Silicon 系列或架构为 `aarch64` 应该更改相关镜像资源。

准备好了 `.env` 之后，执行 `docker-compose up` 以启动环境（加上 `-d` 可以后台显示），关闭环境则是 `docker-compose down`（你不应该直接 Stop，除非你没有对其做任何修改）；当启动环境后从输出的日志文件中没有任何报错时，你可以开始完成 `check_deps.py` 了。

当你完成了 `check_dps.py`，运行以下指令:

```bash
cd 1-count
python check_dps.py
```

如果正确执行，你会看到如下输出，具体的 `ip_address` 和 `num_tasks` 会有所不同，但你需要确认的是，应该会有 _`.env.NUM_WORKERS` + 1_ 条数据

```text
Tasks executed
    172.63.0.3 tasks on 45
    172.63.0.4 tasks on 46
    172.63.0.2 tasks on 9
```

### baseline 和并行化

在开始完成 `count.py` 之前，你应该优先运行 `baseline.py`，然后将运行时间记入到 `score.txt` 中。

在完成 `count.py` 之前，你应该了解开始计算运行时间的部分，在当前 baseline 中，环境的 `setup` 阶段你不应该纳入计时，即从计算任务开始被分配执行时开始计时。

当你完成后运行即可，并将其运行时间记入到 `score.txt` 中(**注：该时间是由你上传的 `count.py` 文件运行后的成绩**）。

一下是运行 `python count.py` 之后的输出实例：

```text
arranging the worker...
start to calculating...
Time: 20.55s
Result Is Accepted: True
```

**你需要特殊注意最后一行的输出是否可被接受。**

### 不同资源的分配 (Optional)

如果你尝试了其他方案，如修改 `ray.remote` 的默认参数或调节 `.env` 中的 `NUM_WORKERS` 和 `NUM_CPU_WORKER` 字段的值，你可以在 `score.txt` 后追加内容并做好相应的标注，即该成绩是修改什么内容后得到的。

你也可以就此写一篇 `note.md` 来分析和思考这些变化的原因。
