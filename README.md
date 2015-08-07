###  直接上中文

他的由来很简单，有时服务器之间会做文件的传输, 但可能是种种原因，或因为scp麻烦，或对端没有外网，或各种.....

运行
```
[ruifengyun@devops porter ]$ python server.py 9090
INFO:root:Serving HTTP on 0.0.0.0 port 9090 ...

```

你可以大考浏览器去下载上传,也可以直接用curl来进行上传

```
curl -F "file=@app.py" http://127.0.0.1:9090/
```

下载的方法

```
curl -O http://127.0.0.1:9090/upload/app.py
```

