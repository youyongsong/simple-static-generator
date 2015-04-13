## 项目1
使用django制作blog，项目托管到了github上，关于项目的说明可以在github上的README中看到：
     
- github地址：https://github.com/youyongsong/django-blog     
- 在线演示地址：http://youyongsong-blog.herokuapp.com


## 项目2
该项目我制作的是一个简单的静态网页生成器，项目在`md2web`目录下，其核心文件是该目录下的`convert.py`文件。该项目可以将`src`目录及其子目录下的所有的markdown文件转换成html文件，并根据其目录结构生成索引`index.html`，生成结果将会保存在`build`目录下。    
具体使用方法如下：    

### 安装项目所需的python环境
1. python3.4，该项目是在python3.4环境下开发的，如果使用python2运行可能会出现一些问题。    
2. `markdown`，项目用到了`markdown`这个package，可用`pip install markdown`进行安装。    

### 准备项目所需的素材
该项目是要对`convert.py`同目录下的`src`目录下的markdown文件进行处理，所以需要讲要处理的markdown文件放到`src`目录下。在我上传的项目中，已经在`src`目录下放了测试要用的markdown文件，所以此步骤可以滤过。    

### 运行项目    
进入`md2web`目录，即`convert.py`所在的目录，然后运行：    

```
python convert.py
```
运行命令后便会在此目录下生成一个`build`目录，和一个`index.html`文件。打开`index.html`文件即可。    

### 项目结果    
生成的索引即`index.html`，如下：    
![](http://cl.ly/image/2y0q353b1y0O/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202015-04-09%20%E4%B8%8B%E5%8D%881.00.38.png)    

点击索引中的文件即可进入文件的详情页面，如下：    
![](http://cl.ly/image/3S3D18461x0C/%E5%B1%8F%E5%B9%95%E5%BF%AB%E7%85%A7%202015-04-09%20%E4%B8%8B%E5%8D%881.03.31.png)    
