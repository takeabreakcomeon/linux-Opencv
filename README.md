# linux-Opencv

opencv的安装过程  调用摄像头 处理图像
## opencv 安装
Linux从源码编译安装大体就是配置，编译，安装三步，下面看看OpenCV的编译安装过程。（安装过程参考：https://www.linuxidc.com/Linux/2017-02/141157.htm）
### 安装依赖环境

本地编译软件并不能自动下载依赖环境，因此需要手动安装，执行以下命令即可

sudo apt-get update

sudo apt-get install build-essential

sudo apt-get install cmake

sudo apt-get install libgtk2.0-dev

sudo apt-get install pkg-config

sudo apt-get install python-dev python-numpy

sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev


### 获取源代码

opencv：https://github.com/opencv/opencv 

opencv_contrib：https://github.com/opencv/opencv_contrib

为方便起见，新建一个opencv文件夹  将源代码解压到该文件件下。可以在该文件夹下利用gitclone直接下载，也可以下载zip解压。在解压opencv源码的文件夹下新建一个release文件夹用于存放编译的临时文件，在release文件夹中进行编译。

### 编译安装

这里我们使用默认的配置，安装路径默认为 /usr/local ，执行以下命令

cd ~/opencv/opencv/release/

sudo cmake -D CMAKE_BUILD_TYPE=RELEASE 
	
   -D CMAKE_INSTALL_PREFIX=/usr/local 
   
   -D OPENCV_EXTRA_MODULES_PATH=~/opencv/opencv_contrib/modules 
   
   -D INSiTALL_PYTHON_EXAMPLES=ON 
  
   -D BUILD_EXAMPLES=ON ..

sudo make -j4

sudo make install

sudo ldconfig

注意：
* CMAKE_BUILD_TYPE是编译方式

* CMAKE_INSTALL_PREFIX是安装目录

* OPENCV_EXTRA_MODULES_PATH是加载额外模块

* INSTALL_PYTHON_EXAMPLES是安装官方python例程

* BUILD_EXAMPLES是编译例程（这两个可以不加，不加编译稍微快一点点，想要C语言的例程的话，在最后一行前加参数INSTALL_C_EXAMPLES=ON ）

* 结尾  ..    不要漏掉

* cmake的语句格式为cmake -DOPENCV_EXTRA_MODULES_PATH=<opencv_contrib>/modules <opencv_source_directory>，注意对应好文件的地址，-j4选项表示使用4个线程编译，如果你的CPU有4个物理核心，可以加速编译，需要根据CPU的核心数配置。

## linux摄像头的调用

### 检测是否找到usb设备（如果直接调用笔记本摄像头，跳过该步骤）
执行以下命令：

lsusb

如果没检查到，可能是驱动没安装，进行内核编译增加UVC支持。（参考https://blog.csdn.net/qq_42041303/article/details/85470936）

### 检查相机端口

执行以下命令

ls -la /dev/vid* 

可能会显示以下结果：

crw-rw----+ 1 root video 81, 0 Feb 12  2016 /dev/video0
crw-rw----+ 1 root video 81, 3 Jul 18 13:28 /dev/video1

其中 video0 是tx2自带摄像头， video1为usb摄像头

## 利用opencv调用摄像头


