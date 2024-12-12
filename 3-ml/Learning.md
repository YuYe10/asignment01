# 学习体会
## 1-count
### 一、完成check_dps.py

1.提交job到ray cluster

~~~bash
RAY_ADDRESS='http://127.0.0.1:8265' ray job submit --working-dir . -- python <name_of_script>.py
~~~

2.完成count.py

