###  介绍

他的由来很简单，有时服务器之间会做文件的传输, 但可能是种种原因，或因为scp麻烦，或对端没有外网，或各种.....

### 安装
```
git clone git@github.com:rfyiamcool/fileporter.git
cd fileporter;python setup.py install

或者.

pip install fileporter
```
### 方法

运行

```
[ruifengyun@devops fileporter ]$ python fileporter.py 9090
INFO:root:Serving HTTP on 0.0.0.0 port 9090 ...

and ,same as SimpleHTTPServer method

[ruifengyun@devops ~ ]$ python -m fileporter.server 8080
INFO:root:Serving HTTP on 0.0.0.0 port 8080 ...

```

查看当前的文件列表
```
curl http://127.0.0.1:9090/

```

你可以打开浏览器去下载上传,也可以直接用curl来进行上传

```

curl -F "file=@app.py" http://127.0.0.1:9090/
```

下载的方法

```
curl -O http://127.0.0.1:9090/app.py
```

下面是浏览器的截图... 
![Alt text](fileporter.jpg)


### to do list
1. fix run path
2. 配套一个客户端，支持断点续传和多线程下载。 
