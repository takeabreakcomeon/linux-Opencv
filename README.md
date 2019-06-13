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

### 创建编译目录

为了方便，我们在home目录下创建一个opencv的目录，其下包含build，source，contrib三个目录，其中source作为opencv的源码目录，contrib作为附加模块的目录，build为编译生成的二进制文件的存放目录，执行以下指令：

cd

mkdir opencv

cd opencv

mkdir build source contrib

### 获取源代码

opencv：https://github.com/opencv/opencv 

opencv_contrib：https://github.com/opencv/opencv_contrib

将源代码解压到对应的目录

### 编译安装

这里我们使用默认的配置，安装路径默认为 /usr/local ，执行以下命令

cd ~/opencv/build

cmake -DOPENCV_EXTRA_MODULES_PATH=../contrib/modules ../source

make -j4

sudo make install

注意：cmake的语句格式为cmake -DOPENCV_EXTRA_MODULES_PATH=<opencv_contrib>/modules <opencv_source_directory>，在cmake的过程中如果自动下载文件但是速度较慢的话参考这篇文章【OpenCV】使用cmake生成MakeFile时下载文件，-j4选项表示使用4个线程编译，如果你的CPU有4个物理核心，可以加速编译，需要根据CPU的核心数配置。
