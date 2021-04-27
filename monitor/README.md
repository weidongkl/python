# monitor

## 功能
监控 dde-file-manager
在dde-file-manager占用内存过大时，kill dde-file-manager。
## 源码使用安装
```
git clone https://gitlabxa.uniontech.com/ut001996/monitor.git
cd monitor
python3 setup.py install
nohup weidong-monitor  &
# 提高进程优先级
sudo renice -8 -p $(ps -ef | grep weidong-monitor | grep -v grep | awk '{print $2}')
```
## 打包方法
打包命令如下:
```
python3 setup.py sdist bdist_wheel
```
执行完命令之后，会生成`dist/{weidong_monitor-0.0.2-py3-none-any.whl,weidong-monitor-0.0.2.tar.gz` 文件.可以使用 pip3 命令安装此`.whl`或`.tar.gz`文件。
当然，也可以上传至 pypi.org 或者自己的私有仓库 

