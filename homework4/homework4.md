#Homework4
##*摘要
在这次作业中，我做了两个题目。

第一个是第一题，解决了一维重力场中物体速度随时间的变化，需要用户输入初始速度，持续时间，和每次计算的时间间隔。

第二个是第四题，解决了两种原子核耦合衰变的各种原子核数目随时间的变化，需要用户输入两种原子核的数目，两种原子核的衰变常数，衰变持续时间，以及每次计算的时间间隔。
##*正文

[这是第一题源代码](https://github.com/qinxiaochord/computationalphysics_N2013301020086/blob/master/homework4/1.py)

[这是第四题源代码](https://github.com/qinxiaochord/computationalphysics_N2013301020086/blob/master/homework4/4.py)

第一题和第四题的计算方法完全相同，因此，在这里只介绍第一题的计算方法，第四题只不过是两个耦合的方程罢了。

首先，先创建两个空的list来储存每个时刻的速度和每个时刻，之后初始化t0和给出地球表面重力加速度g。

![图1.1](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/1_1.png)

之后让用户输入t_end（表示结束时间），dt（表示每次计算的时间间隔），v0（表示初始速度）。

![图1.2](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/1_2.png)

再然后按照公式

$\frac{dv}{dt}=g$

将每次计算的结果添加到之前创建的list中去。

![图1.3](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/1_3.png)

最后打印出两个list和画图。

![图1.4](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/1_4.png)
##*结果

以下是结果的图片：

第一题数据

![图1.5 第一题数据](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/1%E6%95%B0%E6%8D%AE.png)

第一题图像

![图1.6 第一题图像](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/v_vs_t.png)

第四题数据

![图1.7 第四题数据](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/4%E6%95%B0%E6%8D%AE.png)

第四题图像

![图1.8 第四题图像](https://raw.githubusercontent.com/qinxiaochord/computationalphysics_N2013301020086/master/homework4/NA_NB_vs_t.png)

