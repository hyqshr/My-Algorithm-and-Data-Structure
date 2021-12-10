Notes for Introduction to Algorithms

# 算法导论笔记

- The notes are sorted according to the teaching order of NEU CS 5800 **Prof. Virgil Pavlu**, some chapters of the original book are skimmed.
- 笔记按照NEU CS 5800 **Prof. Virgil Pavlu** 的教授顺序来排序，有掠过原书的一些章节。

- 如果不支持markdown可以下载pdf。

- 持续更新中，有一些图片还未上传到图床。



- notes by  ```Yiqiu Huang```



# 3.  Growth of Funcitons

## 3.1  **Asymptotic notation**

**What is $T(n)$?**

- we call it T(n) = number of computational steps required to run the algorithm/program for input of size n 

- we are interested in order of growth, not exact values 
  -  for example T(n) = Θ(n2) means quadratic running time  
  -  T(n) = O(n logn) means T(n) grows not faster than CONST*n*log(n)



Why **Asymptotic notation**?

>Even when we use asymptotic notation to apply to the running time of an algorithm, we need to understand which running time we mean.





![image-20211025143113872](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025143113872.png)



### 3.1.1 $\Theta$ Notation

原文定义如下：

>For a given function g(n), we denote by $\Theta$(g(n)) the set of functions:
>
>
>
>$\Theta(g(n))$ = \{$f(n)$: there exist positive constants $c_1$, $c_2$, and $n_0$ such that $0\leq c_1g(n) \leq f(n) \leq c_2g(n)$ for all n $\geq$ n0 \}
>
>
>
>如果满足如上条件，我们说 g(n) is an **asymptotically tight bound** for f(n) 



简单来说就是n到一定大小以后($n \geq n_0$,$n_0$是个常数), **在常数范围内**, $f(n) = g(n)$,($0\leq c_1g(n) \leq f(n) \leq c_2g(n)$), 看下图(a)。



注意，$\Theta(g(n))$ 本身**描述的是一个集合**，所以你可以这么写：
$$
f(n) \in \Theta(n)
$$


不过我们习惯这么写： 
$$
f(n) = \Theta(n)
$$
这样写有自己独特的优势。



$\Theta$ Notation 是 **asymptotically tight bound**，最简单的说，$\Theta$ notation 就像是 等于号


$$
\Theta : =
$$




### 3.1.2 $O$ Notation



原文定义如下：

>For a given function g(n), we denote by $\Theta$(g(n)) the set of functions:
>
>
>
>$\Theta(g(n))$ = \{$f(n)$: there exist positive constants $c$ and $n_0$ such that $0\leq f(n) \leq c g(n)$ for all n $\geq$ n0 \}
>
>
>
>如果满足如上条件，我们说 g(n) is an **asymptotically upper bound** for f(n) 



简单来说就是n到一定大小以后($n \geq n_0$,$n_0$是个常数), **在常数范围内**, $f(n) \leq g(n)$, 看图(b)。



最简单的说，$O$ notation 就像是小于号，它描述的是上界。


$$
O : \leq
$$

>平时我们习惯用大O表示法来表示runtime，比如寻找一个数组的最大值，我们说runtime 是 O(n)；
>
>这么说不完全严谨，因此O(n)描述的是上界(upper bound)，无法说明how tight that bound is, 你说寻找最大值的算法是$O(n^2)$,$O(n^3)$也没问题。



### 3.1.3 $\Omega$ Notation



原文定义如下：

>For a given function g(n), we denote by $\Theta$(g(n)) the set of functions:
>
>
>
>$\Theta(g(n))$ = \{$f(n)$: there exist positive constants $c$ and $n_0$ such that $0 \leq c g(n) \leq f(n)$ for all n $\geq$ n0 \}
>
>
>
>如果满足如上条件，我们说 g(n) is an **asymptotically lower bound** for f(n) 



简单来说就是n到一定大小以后($n \geq n_0$,$n_0$是个常数), **在常数范围内**, $f(n) \geq g(n)$, 看图(b)。


$$
\Omega : \geq
$$


## 3.2 例题



1. 

![image-20211025150247482](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025150247482.png)



**答案：**

![image-20211025151610012](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025151610012.png)



本质上，你要证明常数存在，来证明公式正确。



2. 

![image-20211025150257654](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025150257654.png)



类似的技巧：

![image-20211025152145243](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025152145243.png)



![image-20211025152441901](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025152441901.png)



![image-20211025152454525](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025152454525.png)



# 2.3.1 Divide-and-conquer

分治法：

>**Divide** the problem into a number of subproblems that are smaller instances of the
>
>same problem.
>
>
>
>**Conquer** the subproblems by solving them recursively.
>
>
>
>**Combine** the solutions to the subproblems into the solution for the original problem.



与我们熟悉的 **Mergesort** 一一对应：

>**Divide**: 把长度为 n 的序列切分为两个长度为 $\frac{n}{2}$ 的序列
>
>**Conquer**: 递归的调用mergesort来sort sequence。(原文：Sort the two subsequences recursively using merge sort)
>
>**Combine:** 合并两个sorted sequence



## 2.3.2 **Analyzing divide-and-conquer algorithms**





<img src="C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211021012239751.png" alt="image-20211021012239751" style="zoom: 80%;" />



Suppose that our division of the problem yields **a** subproblems, each of which is **1/b** the size of the original.



- **注意，Mergesort的a = b = 2**, **很多分治法a 并不等于 b 更不等于 2
- 注意后面这句话: each of which is **1/b** the size of the original 他的意思是每个子问题的size都是原来的1/b，那么随着递归的进行，子问题的size就是:

$$
\frac{n}{b} -> \frac{n}{b^2} ->\frac{n}{b^3} -> ... \frac{n}{b^?}
$$

*可以思考一下这个 **?** 应该是什么*





用白话来说就是，mergesort产生了2个size是(n/2)的subproblem。



假设mergesort的runtime 是**T(n)**,我们有 **a** 个size 为**b/n** 的子问题，因此我们需要 **aT(n/b)** 来解决他们。

除此之外，我们需要 D(n) 来divide the problem into subproblem, 以及 C(n) 来combine我们的solution from all subproblem, 我们的总时间为：



![image-20211021020351632](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211021020351632.png)



这段比较重要，还是原汁原味吧：



>**Divide:** The divide step just computes the middle of the subarray, which takes
>
>constant time. Thus, D.n/ D ‚.1/.
>
>**Conquer:** We recursively solve two subproblems, each of size n=2, which contributes 2T(n/2) to the running time.
>
>**Combine:** We have already noted that the MERGE procedure on an n-element
>
>subarray takes time ‚.n/, and so C.n/ D ‚.n/.



>**Divide:** mergesort 在 diide 时只计算出中位数，所以是contant time, D(n) = 1
>
>**Conquer:** 我们递归的解决两个子问题，每一个子问题的size是 n/2, 因此是 2T(n/2)
>
>**Combine:** combine的本质就是遍历，谁小谁先进sorted array, 因此 $C(n) = \Theta(n)$



因此：



![image-20211021021214338](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211021021214338.png)





![image-20211021022324915](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211021022324915.png)



## 	2.3.3 求解分治法的时间复杂度



递归法往往能写成以下的格式：



<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025161742046.png" alt="image-20211025161742046" style="zoom:80%;" />

主要有三种方法求解分治法的时间复杂度

>In the **substitution method**, we guess a bound and then use mathematical in
>
>duction to prove our guess correct.
>
>
>
>The **recursion-tree method** converts the recurrence into a tree whose nodes
>
>represent the costs incurred at various levels of the recursion. We use techniques
>
>for bounding summations to solve the recurrence.
>
>
>
>The **master method** provides bounds for recurrences of the form
>
>$T(n) = aT(\frac{n}{b}) + f(n)$



### 1. subtitution method



![image-20211025161954364](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025161954364.png)



![image-20211025162329705](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025162329705.png)

![image-20211025162434114](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025162434114.png)

![image-20211025162454849](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025162454849.png)

![image-20211025162502931](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025162502931.png)

### 2. recursion-tree method



![image-20211025164738578](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025164738578.png)



### 3. **Master Theorum**

使用**Master Theorum**可以快速求出常见递归的时间复杂度。



比较重要，比较实用，比较递归参数的大小得到时间复杂度：



<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025165224255.png" alt="image-20211025165224255" style="zoom:80%;" />



Binary search, Mergesort 的runtime 可以轻松的求出。







#### 3.1 Why MT have 3 cases



首先求出递归的数学表达：

![image-20211025173147044](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025173147044.png)



对于关键项



![image-20211025173606212](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025173606212.png)



来说，**有三种表达 <1,=1,>1,so three**



![image-20211025173822634](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025173822634.png)



![image-20211025174214744](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025174214744.png)

![image-20211025174220736](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025174220736.png)



# 6. Sorting



![image-20211029162717277](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211029162717277.png)



## 6.1. Binary Search



算法本身不做介绍。



worst running time is O(log n)



二叉树的本质是一种**比较算法**, 在这里先引入这个概念:



<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025234445058.png" alt="image-20211025234445058" style="zoom:80%;" />



## 6.2. Selection Sort/Bubble sort/Insertion sort

**Insertion sort**



![image-20211029162544691](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211029162544691.png)

## 6.3 Heap sort: 堆排序

### 6.3.1 MAX-HEAPIFY

**最大堆性质：**

 In a **max-heap**, the **max-heap property** is that for every node i other than the root:

![image-20211026155535675](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211026155535675.png)

最小堆性质与之相反；



为了满足最大堆性质，你需要调用:

![image-20211026155823020](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026155823020.png)

这段代码的逻辑就是找出 $A[i], A[LEFT(i)], A[RIGHT(i)]$的最大值；

- 如果最大值是$i$，那么左右子树小于$i$, 满足max-heap property,无事发生。
- 如果不是，将$i$与largest 交换；交换后当前node满足max-heap, 但是子树不一定满足；因此对子树继续进行max-heapify



![image-20211026163224130](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026163224130.png)



**MAX-HEAPIFY** 复杂度分析：



![image-20211026163928877](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026163928877.png)

![image-20211026163940617](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026163940617.png)

### 6.3.2 Build-max-heap



根据heap(二叉树)的性质，$A[(\frac{n}{2} + 1) ... n]$都是叶节点；因此从$ \frac{n}{2}$ downto 1进行heapify

![image-20211026171240306](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026171240306.png)



这样就完成了BUILD-MAX-HEAP。



下面来自例题：

![image-20211026172117945](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026172117945.png)

答案：

![image-20211026172101889](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026172101889.png)

## 6.3.3

Heapify -> 得到最大值 ->换到最后一位，不再管他，size - 1 -> 循环

![image-20211026203740175](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026203740175.png)



![image-20211026204052270](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026204052270.png)



## 6.4 Quicksort



**A  divide-and-conquer algorithm with worst-case running time of $\Theta(n^2)$ ,expected in $O(n \cdot lgn)$.**



![image-20211026210648741](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026210648741.png)

![image-20211026210659307](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026210659307.png)



![image-20211026214751401](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026214751401.png)

### 6.4.1 Partition



**Partition 是 quicksort 最重要的机制**。



![image-20211026210829980](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026210829980.png)

Partition 会选择 x = A[r] 作为 pivot element。你要理解的是在Partition的过程中，有四个区域，先理解这个思路，伪码就能看懂了：

![image-20211026213059537](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026213059537.png)

[j,r-1] 还没看到的区域

[p, i] 小于pivot 的区域

[i,j] 大于pivot的区域

[r] **pivot element**

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026212905439.png" alt="image-20211026212905439"  />



注意，partition返回的是i + 1.



**Worst-case partitioning**

The worst-case behavior for quicksort occurs when the partitioning routine produces one subproblem with $n - 1$ elements and one with 0 elements.



# 7. Linear Sort



## 7.1. Counting Sort

![image-20211026235403867](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026235403867.png)

## 7.2. Radix sort

![image-20211026235828458](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026235828458.png)

![image-20211026235835161](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211026235835161.png)



## 7.3. Bucket Sort

老师讲的很少，这块不复习了。



![image-20211027002342731](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211027002342731.png)



# 8.1 Lower bounds for sorting



### 为什么主流comparison sort(比较算法,如快排，mergesort,heapsort)的time complexity 为nlogn?

常见的算法主要是比较算法(**comparison sort**)，比如mergesort在merge的部分需要比较两个数字的大小来排序。comparison sort 可以用下图的例子来类比：

![image-20211001003323500](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001003323500.png)

求出树的高度h**(i.e., 抵达leaf的worst case时间)**,就是排序的worst case时间。

输入n的permutation 为n!, 参考下图的决策树，运行时间即为h，可以得出
$$
h = \Omega(n lgn)
$$
摘一段原文：

![image-20211001003938217](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001003938217.png)



为什么　**$lg(n!) = \Omega(n \cdot lg n)$** ? 下面给出书中的证明。（看看就得了）



### 公式3.19: Factorial 的时间复杂度

![image-20211001005319481](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001005319481.png)

Some intuition about why:
$$
lg(n!) = \Theta(n\cdot lgn)
$$
你需要记住

![image-20211001005135146](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001005135146.png)



and



![image-20211001005504205](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001005504205.png)



![image-20211001004725166](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211001004725166.png)

# 9 Medians and Order Statistics

#### 这一章节主要find $i_th$ smallest number的问题

**在选择最小值的算法上，我们都知道**：

![image-20211002221151029](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211002221151029.png)

遍历数组，经过n-1次的比较我们可以找到最小值。***This is the best we could do.***



## 9.2 Selection in expected linear time

The general selection problem appears more diffificult than the simple problem of finding a minimum. Yet, surprisingly, the asymptotic running time for both problems is the same:
$$
\Theta(n)
$$

**RANDOMIZED-SELECT**类似quickSort,也是一种**divide-and-conquer** alg. 



The following code for **RANDOMIZED-SELECT** returns the **i** smallest element of array A[p...r]



![image-20211002221646438](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211002221646438.png)



- Line 1 & Line 2: 如果array长度为1，那直接返回array中的值

- Line3: 类似quickSort的partition, 选择pivot，让A[p...q-1]的小于pivot, 让A[q+1,r]的值大于pivot, **A[q]**就是pivot number

- Line4: 计算k(即A[p...q-1]的长度 + 1)

- Line5: 如果 i == k,即你要的i th 等于 k,找到了答案，返回A[q]

- Line7, 8,9: 否则，根据 i与k的关系继续调用**RANDOMIZED-SELECT**(if i>k, the desired element will lies in high partition part)

  

The worst-case running time for RANDOMIZED-SELECT is 
$$
\Theta(n^2)
$$

## 9.3 **Select** algorithm with worst case runtime O(n)



**select algorithm 应该就是median-of-medians,但是没有在wiki上得证。**



大致思路：

* Divide the n elements of the input array into n/5 groups of 5 elements each gourp
* Find the median of each of the n/5 groups by insertion sorting




通常找第 $i^{th}$ 小的数字比找最小的数字更难，而The Median-of-medians Algorithm的时间复杂度:**O(n)**。



#### The Median-of-medians/Select Algorithm(找第 $i^{th}$ 小的数字)

> Use a **divide and conquer** strategy to efficiently compute **the $i^th$ smallest number** in an unsorted list of size n.



好文：https://brilliant.org/wiki/median-finding-algorithm/

![](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003015239429.png)

![image-20211003000642719](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003000642719.png)

##### EXAMPLE of Median-Median Algorithm：**来跟一遍例子就懂了：**

​		给定A的，找到4th smallest element:

![image-20211003015419858](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003015419858.png)

把A分成**n/5**份，保证每个subgroup有5个元素

![image-20211003015450341](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003015450341.png)

分别求中位数：

![image-20211003015605490](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003015605490.png)

Sort M:

![image-20211003015649100](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003015649100.png)



求出M 中的中位数 len(M)/2 = 1, which is **76** (这一步就是所谓median-of-medians)



使用**76**作为pivot, **partition(A)**，左边元素小于pivot index(76的idx是5)，右边大于pivot index;

![image-20211003020016241](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003020016241.png)

**76**的index是5, **5 > 3**, 所以继续，在左半边(p, q-1)继续partition，也就是

![image-20211003020910176](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003020910176.png)

![image-20211003021005215](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003021005215.png)



最后只剩5个元素的时候会直接排序，书中说小于5个的元素排序时间复杂度是n，idk y。



*注：sort小于5的array时间为O(n)? WTF? 这点我也没搞懂*



#### 算法分析 The Median-of-medians

![image-20211003022747950](C:\Users\Administrator\AppData\Roaming\Typora\typora-user-images\image-20211003022747950.png)

详细分析参考上方的原文链接。以下为intuition：

- **T(n/5)** + O(n):

  我们把n分成了n/5的subproblem, partition需要上述的时间，参考quickSort。

- **T(7n/10)**

  在M(median list, 参考example M)中，M的长度为**n/5** ,因此M中有一半的元素小于p(M的中位数，也就是中位数的中位数)，也就是n/10，这一半的元素本身又有2个元素小于自己，因为这些元素本身是median of 5 element，因此有n/10 + 2* n/10 = 3n/10 的元素小于p。

  因此在worst case情况下，算法每次都会recurse on the remaining 7n/10的元素。

根据master thoerum, 得出time complexity O(n)

# 16 Greedy Algorithms

**Intro**: why greedy algorithm?

>For many optimization problems, **using dynamic programming to determine the best choices is overkill**; 
>
>A **greedy algorithm** always makes the choice that looks best at the moment. That is, it makes a **locally optimal** choice **in the hope that** this choice will lead to a **globally optimal** solution.
>
>**Greedy algorithms do not always yield optimal solutions**, but for many problems they do

## 16.1 经典**例题1: ** An activity-selection problem 

目标：我们要选择最大activities数量的集合，activities时间不能重合。（maximum-size set of activities.）



<img src="C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211027142307170.png" alt="image-20211027142307170" style="zoom:67%;" />



我们有n个activities,![image-20211008000112473](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211008000112473.png) 每个activity **a <sub>i</sub>** has a **start time** **f <sub>i</sub>** and a **finish time** **s <sub>i</sub>** 

![image-20211007235424245](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211007235424245.png)



你选择的集合中，**a <sub>i</sub>** 和**a <sub>j</sub>** 需要是兼容的(compatible), 也就是他们**时间区间 [si,fi] 不能有重合**。



比如 set :{**a <sub>1</sub>**, **a <sub>2</sub>**} 是一个不合格的set, 因为 **a <sub>1</sub>** 的区间[1,4] 和 **a <sub>2</sub>** 的区间[3,5] 就在[3,4]上有重合，我们要避免这样的overlap,选出最大的子集。



贪心算法的核心在于，我们要找出最好的**greedy choice**。在这个问题中，我们每一步都需要:

>we should choose an activity that leaves the resource available
>
>for as many other activities as possible.



这句话的意思在后来的另一个例子找硬币中也能体现出来，现在先往下走。



>**Greedy Algorithm的核心**：
>
>
>
>- **Greedy choice**: 每次都寻找**最早结束**的activity, Let's call it **a <sub>earliest</sub>**
>- **Subproblem**: only consider activity start after **a <sub>earliest</sub>** have finished. (排除有overlap的activity)
>
>
>
>***剩下的，交给递归recursive***
>
><img src="C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211008004254723.png" alt="image-20211008004254723" style="zoom:80%;" />
>
>
>
>(#注意，**书中假设activity list: n已经按照finish time list: f 进行升序的排序**），因此time complexity O(n))：
>
>> *It also assumes that the input activities are ordered by monotonically increasing finish time.*

看看就行：

经过经典的递归greedy algorithm解法，经典的下一步就是**把rucursive变成iterative**的解法。



![image-20211008005753258](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211008005753258.png)



## 16.1 经典**例题2: ** An activity-selection problem 



## 16.2 总结：Elements of the greedy strategy



贪心算法的核心性质：



**Greedy-choice property**

The first key ingredient is the **greedy-choice property**: we can assemble a globally

optimal solution by making locally optimal (greedy) choices.



这个性质比较好理解，这也是greedy和DP的主要区别。



**Optimal substructure**

A problem exhibits **optimal substructure** if an optimal solution to the problem

contains within it optimal solutions to subproblems. 



这个性质可能需要时间消化，以activity-selection问题为例：



> if an optimal solution to subproblem $S_{ij}$ includes an activity $a_k$, then it must also contain optimal solutions to the subproblems $S_{ik}$ and $S_{kj}$



下方是书中给出的步骤：

![image-20211009000335223](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211009000335223.png)

**总结**

- 贪心算法only make **locally optimal choiceœ**, 部分的贪心算法不能保证走向 global-optimal solution, 但我们只关心那些能保证走向global-optimal solution的算法。
- 贪心算法的核心在于寻找strategy, 你需要证明你的贪心策略是正确的。

## 16.3 [optional] Corectness of greedy algorithm

证明贪心算法需要证明以下两个性质

>**Greedy-choice property**
>
>The first key ingredient is the **greedy-choice property**: we can assemble a globally optimal solution by making locally optimal (greedy) choices.
>
>**Optimal substructure**
>
>A problem exhibits **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.

![image-20211029163303335](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211029163303335.png)



![image-20211029163508292](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211029163508292.png)



![image-20211029163101312](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211029163101312.png)





# 15 Dynamic Programming

>- **Dynamic programming, like the divide-and-conquer method, solves problems by**
>
>**combining the solutions to subproblems.**
>
>- **In contrast, dynamic programming applies when the subproblems overlap—that is, when subproblems share subsubproblems.:**
>
>>- **divide-and-conquer** algorithm **does more work than necessary**, repeatedly solving the common subsubproblems.
>
>>- **dynamic-programming** algorithm solves each subsubproblem just once and then **saves its answer in a table**, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem.

![image-20211014012344213](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014012344213.png)

## 15.1 EX: Rod cutting

切绳子问题定义如下：

给定一个总长度为n的绳子，给定价格 $p_i$ 与 长度 $i$ 的对应表，如下图所示。

Task: **如何切分绳子，使得总价值 $r_n$ 最大化？**

![image-20211014012725557](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014012725557.png)

比如给定长度为4的绳子，绳子可以切分的**长度**和根据上图计算得出的**总价值**分别如下：

![image-20211014020025941](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014020025941.png)

可以看出 (c)的总价值为10，是最大的。

切绳子问题展现出了**optimal substructure**: 

原始问题是 problem of **size(n)**, 当我们第一次cut之后，我们就在解决两个独立的子问题。

>optimal solutions to a problem incorporate optimal solutions to related subproblems, which we may solve independently.
>
>i.e. 子问题的最优解被包含在了全局问题的最优解中。

**Method 1: Brute force**

长度为n的绳子共有 $2^{n-1}$ 种切法，算出最大值。

**Method 2: Recursive top-down implementation**

![image-20211014022815149](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014022815149.png)

```
@param:
**p** : array p[1..n] of price

n: 长度n

#comment
3：init max value to -infinity
4-5: compute max value q

```

**CUT-ROD is very inefficient.** it solves the same subproblems repeatedly.

下图展示了 CUT-ROD(p, 4)的递归，可以看到**相同的子问题被反复的计算**。

![image-20211014031113722](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014031113722.png)

时间复杂度T(n) = $2^n$

**Method 3 dynamic programming for optimal rod cutting**

动态规划出现了！

核心思想：每个子问题只解决一次，使用额外的空间来保存子问题的solution。

**We just look it up, rather than re-compute it.**

It is a **time-memory trade-off**.

>There are usually two equivalent ways to implement a dynamic-programming
>
>approach.
>
>The fifirst approach is **top-down with memoization**.
>
><details>
>The first approach is top-down with memoization. In this approach, we write the procedure recursively in a natural manner, but modifified to save the result of
>each subproblem (usually in an array or hash table). 
>The procedure now first checks to see whether it has previously solved this subproblem. If so, it returns the saved value, saving further computation at this level; if not, the procedure computes the value in the usual manner. We say that the recursive procedure has been memoized;it “remembers” what results it has computed previously.
>
>
>
>
>The second approach is the **bottom-up method**. 
>
><details>
>This approach typically depends on some natural notion of the “size” of a subproblem, such that solving any particular subproblem depends only on solving “smaller” subproblems. We sort the subproblems by size and solve them in size order, smallest first. 
>When solving a particular subproblem, we have already solved all of the smaller subproblems its solution depends upon, and we have saved their solutions. We solve each subproblem only once, and when we first see it, we have already solved all of its prerequisite subproblems.  

>简单来说，二者差别如下：
>
>**top-down**方法先检索是否有该subproblem的答案；
>
>​		如果有，使用该答案。
>
>​		**否则, 计算该答案，进入递归。**
>
>
>
>而**bottom-up**方法使用问题大小的**自然顺序**(natural notion of the size of problem)，**从最小的问题开始， 自底向上 的逐一解决，**因此解决到大问题时，之前的小问题已经解决完了。
>
>*原文的详细定义点开上方折叠。*

**Pseudocode for the top-down CUT-ROD procedure: **

**top-down:**

![image-20211014032957360](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014032957360.png)

![image-20211014033008113](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014033008113.png)

**bottom-up**:

![image-20211014034126509](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014034126509.png)



下图为**bottom-up** 方法我个人的**部分**演算：




![image-20211014041324605](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014041324605.png)



## 15.2 EX: Matrix-chain multiplication 矩阵连乘问题

我们熟知的矩阵乘法的伪码如下：

![image-20211014141041781](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014141041781.png)



假设我们要连乘矩阵 <$A_1,A_2,A_3,A_4$>, 我们有以下5种方法, i,e, we can fuuly parenthesize the product in 5 distinct ways:

![image-20211014142534859](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014142534859.png)



现在我们来分析假设我们要连乘矩阵 <$A_1,A_2,A_3$> ，他们的维度分别为**<10 x 100, 100 x 5, 5 x 50>**。

**parenthesization ** <$((A_1,A_2),A_3$)> 中，第一次括号内运算会有10 * 100 * 5 = 5000 次运算，然后再有 10 * 5 * 50 = 2500 次运算，总共有**7500**次的运算。

而<$(A_1,(A_2,A_3)$)>,第一个括号 100 * 5 * 50 = 25000次运算，之后有10 * 100 * 50 = **50000** 的运算，总共有**75000**次运算，比第一个快**十倍**。

如下，我们引出**矩阵连乘问题**：

>**Our goal is to determine an order for multiplying matrices that has the lowest cost.**

即，找出最快矩阵连乘的顺序。

假设我们有下方的矩阵：



![image-20211015200424926](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015200424926.png)

注意，其中，矩阵$A_i$的维度是 $p_{i-1} \cdot p_i$.

**Method 1** **brute-force 穷举法**

根据矩阵数量，这是inefficient的递归公式：

![image-20211014151447756](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014151447756.png)

**

**Method 1** **Applying dynamic programming**

记得之前的四个步骤：

![image-20211014152817873](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014152817873.png)

![image-20211014152823215](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211014152823215.png)

现在大概跟一遍：

**Step 1: The structure of an optimal parenthesization**

假设我们有如下**optimal** 的待乘矩阵 $A_i,A_{i+1},...,A_{j}$, 我们在$A_k$ (i < k < j) 将待乘矩阵分开，那么$A_i,A_{i+1},...,A_{k}$ 也一定也是子问题 $A_i,A_{i+1},...,A_{k}$的optimal solution。

因为如果$A_i,A_{i+1},...,A_{k}$ 有更好的方法，那么 $A_i,A_{i+1},...,A_{j}$ 也会有更好的方法，这就形成了contradiction。

上面的方法是反证法（contradiction）。



**Step 2: A recursive solution**

如果我们在$A_k$ (i < k < j) 将待乘矩阵分开，那么我们会得到两个子问题$A_i,A_{i+1},...,A_{k}$ 和 $A_k,A_{k+1},...,A_{j}$；

我们让 **m[i, j]** 来表示全局问题的最优解（即最小的multiplication 次数），两个子问题即为 m[i,k], m[k+1,j]; 

合并两个子问题的product $A_{i..k} \cdot A_{k+1..j}$ 我们需要$p_{i-1} \cdot p_j \cdot p_j$。（$A_i 是 p_{I-1} \cdot p_i$）因此
$$
m[i,j] = m[i,k] + m[k+1,j] + p_{i-1} \cdot p_j \cdot p_j
$$
这样求optimal solution需要知道最优切分点 k 的位置，但是我们不知道。因此我们遍历**k from i to j**！

这样，我们的问题变成了



![image-20211015154110269](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015154110269.png)



**Step 3: Computing the optimal costs**

回顾一下斐波那契数列，斐波那契数列也可以用动态规划来表示；

如果只用递归的方法调用斐波那契数列，递归的过程中，F(5)和F(8)都会重新计算F(4),F(3)....

动态规划的标志就是他储存了已经计算过的答案来防止re-compute。

假设我们有下方的矩阵：



![image-20211015200424926](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015200424926.png)



注意，其中，矩阵$A_i$的维度是 $p_{i-1} \cdot p_i$.

bottom-up approach：

- set $m[i,i]$ = 0  ($m[i,i]$代表矩阵乘以矩阵本身，连子问题都不算，只是trivial), 这也是为什么源码的n-1，n=6的问题我们只需要计算五个就好了
- compute $m[i,i+1]$ for $i = 1,2,...,n-1$ 
- then compute $m[i,i+2]$ for $i = 1,2,...,n-1$ , and so forth

![image-20211015214437068](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015214437068.png)



作为一个bottom-up的DP, 我们每次都在尝试想上计算；比如当算到$m[2,5]$时， 我们其实在做以下事情

![image-20211015204809141](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015204809141.png)

![image-20211015204759059](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015204759059.png)



上图左侧的table即为伪码中的 **m** table， 右边的是 **s** table。



m表只给出了m[i,...,j] 的对应最优计算次数，并没有告诉我们 m[1,6] 的过程应该怎么进行切分；因此我们需要右边的 s table 来告诉我们。

**$s[i,j]$ 记录了每一次的最优切分k。**通过s表递归的寻找k,我们就能知道最优切分。

如果上面你看懂了，下面这三张图你可以跳过。

这代码 $for$ 的我人傻了，因此打印一下结果看看运行顺序：

好一个bottom-up：

![image-20211015214610649](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015214610649.png)



![image-20211015214619634](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015214619634.png)

![image-20211015214637964](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211015214637964.png)

## 15.3 **Elements of dynamic programming**

**Optimal substructure**

> A problem exhibits **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.

有些问题没有Optimal substructure性质，比如给定一个没有权值的**有向图**(directed graph)：

![image-20211019024520633](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211019024520633.png)

现在有两个问题，定义如下：

1. 无权值的最短路径问题（**Unweighted shortest path**）：找到某顶点u到某顶点v的 最少边的数量。

   （英文比较好看懂：Find a path from u to v consisting of the **fewest edges**.）

![image-20211019030340759](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211019030340759.png)



2. 无权值的最长路径问题(**Unweighted longest simple path:**): 找到某顶点u到某顶点v的 最多边的数量。



​		哪个问题有optimal structure呢？



问题1有。



>查缺补漏：图的定义如下：
>
>A directed graph (or digraph) is a set of vertices and a collection of directed edges**(边)** that each connects an ordered pair of vertices**(顶点)**.
>
>一句话说，由**顶点 set:V** 和 **边 set :E**组成
>
>![image-20211019030251773](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211019030251773.png)



**Unweighted shortest path:**3 

Find a path from u to consisting of the fewest

edges. Such a path must be simple, since removing a cycle from a path pro

duces a path with fewer edges.



作者很懒还没写完



## 15.4 本章节书本/作业包含的Leetcode题目



作业以及课本包含一些经典DP的leetcode题目，如下：



>[516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence)
>
>[72. Edit Distance](https://leetcode.com/problems/edit-distance)
>
>[300. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence)
>
>[1143. Longest Common Subsequence](https://leetcode.com/problems/longest-common-subsequence)



>[887. Super Egg Drop](https://leetcode.com/problems/super-egg-drop/) (took me a long while...for real...)
>
>得从brute force开始：
>
>https://leetcode.com/problems/super-egg-drop/discuss/159079/Python-DP-from-kn2-to-knlogn-to-kn
>
>到这位大神的：
>
>https://leetcode.com/problems/super-egg-drop/discuss/158974/C%2B%2BJavaPython-2D-and-1D-DP-O(KlogN)





# 10.  基础数据结构

1. **stack:**

**last-in,first-out**

**Methods: push , pop**



![image-20211109133947144](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211109133947144.png)

2. **queue**



**queue: first-in, first-out**

**Methods: deque, enque**





![image-20211109134032340](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211109134032340.png)



## 1. **Linked List** 

The order in alinked list is determined by a pointer. 



<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211109222840384.png" alt="image-20211109222840384" style="zoom:80%;" />



**Methods: search, insert, delete**

### Search, Insertion, deletion

**搜索：**

![image-20211116165254989](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116165254989.png)

时间复杂度：$O(n)$



**插入：**

注意，这个是从**前面插入**；





![image-20211116165315722](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116165315722.png)

不用遍历，**因此时间复杂度是**$O(1)$



**删除：**

需要先使用Search功能，因此worst case时间复杂度是$O(n)$



 ![image-20211116165750614](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116165750614.png)



## 2. Binary Search Tree:



好像没啥说的



5. Binary Search Tree 

![image-20211109223758932](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211109223758932.png)

![image-20211109223808570](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211109223808570.png)



**inorder tree walk**. This algorithm is so named because it **prints the key of the root of a subtree**

**between printing the values in its left subtree and printing those in its right subtree.**



### 0. Min,Max

**Min**

最小值就是找到最左的节点

![image-20211116140058675](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116140058675.png)

**Max**

最大值就是找到最右的节点 

![image-20211116140113962](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116140113962.png)



### 0.5. Successor and Predecessor

Successor and Predecessor是个啥？

**Successor **

> If all keys are distinct, the successor of a node x is the node with the smallest key greater than x.key.

即，x的successor是刚好大于x的那个节点；

为了找到这个节点：



<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211116140649055.png" alt="image-20211116140649055" style="zoom:80%;" />



我们的目标是找到刚好比x大的元素，所以：

- 如果x的右子树不为空，那么找到右子树中的最小元素即可；

  要找到右子树中的最小元素，对着x.right调用 ``min``方法即可；

- 如果x的右子树是空的，那么sucessor只能在x的头上；此时又有两种情况：

  - 假设y是x的parent, 若x是y的左子树，说明x<y,那么直接返回y;
  - 否则, x是y的右子树，x>y, 再往上走；(如果走到根节点，就会返回NIL)



**Predecessor**

与Successor 相反，Predecessor是刚好小于 x 的节点；

假设我们要找的节点x是存在于树中的。

因此:

- 如果x.left $\neq$ NIL, 那么Predecessor就是x.left中的最大值;
- 否则，Predecessor不存在；

书中BST涉及的一些leetcode:



### 1. Check Balance

> 110.Balanced Binary Tree：https://leetcode.com/problems/balanced-binary-tree/

比较tricky地方在于，检查BST是否平衡，不只是统计根节点的左右子树最大高度差，因为可能发生这种情况：

![image-20211113143558671](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211113143558671.png)

对于根节点来说，height(左子树) - height(右子树)的高度差小于2；

但是对于节点10来说，高度差是2，破坏了平衡；

因此，你需要对**每一个节点**都check balance。



### 2. Insertion

>701. Insert into a Binary Search Tree: https://leetcode.com/problems/insert-into-a-binary-search-tree/



找到位置插入即可，优雅的代码来自：

https://leetcode.com/problems/insert-into-a-binary-search-tree/discuss/180244/Python-4-line-clean-recursive-solution

这哥们老想写成一行，为了可读性我给他展开了：

```python
class Solution(object):
    def insertIntoBST(self, root, val):
        if root == None:
            return TreeNode(val)
        if root.val > val:
            root.left = self.insertIntoBST(root.left,val)
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root
```





### 3. Deletion

> 450. Delete Node in a BST： https://leetcode.com/problems/delete-node-in-a-bst/

原文写的太复杂了，用到了transplant; 因此使用leetcode大哥的；



删除操作有3个case;



- **如果节点没有children, 那么直接删除；**

- **如果节点没有左children, 那么右children直接顶上来;**
- **否则，找到左children中的最大值，并且顶上去；**



代码来自：

https://leetcode.com/problems/delete-node-in-a-bst/discuss/213685/Clean-Python-3-with-comments-in-details

```python
class Solution:
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return
        
        # we always want to delete the node when it is the root of a subtree,
        # so we handle left or right according to the val.
        # if the node does not exist, we will hit the very first if statement and return None.
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        # now the key is the root of a subtree
        else:
            # if the subtree does not have a left child, we just return its right child
            # to its father, and they will be connected on the higher level recursion.
            if not root.left:
                return root.right
            
            # if it has a left child, we want to find the max val on the left subtree to 
            # replace the node we want to delete.
            else:
                # try to find the max value on the left subtree
                tmp = root.left
                while tmp.right:
                    tmp = tmp.right
                    
                # replace
                root.val = tmp.val
                
                # since we have replaced the node we want to delete with the tmp, now we don't
                # want to keep the tmp on this tree, so we just use our function to delete it.
                # pass the val of tmp to the left subtree and repeat the whole approach.
                root.left = self.deleteNode(root.left, tmp.val)
        
        return root
```



**so f\*\*king clean**！

**见过的最优雅代码之一了**！























































































# 11 Hash Table

https://docs.python.org/2/library/functions.html#hash

Python 官方文档：

![image-20211113195642447](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211113195642447.png)

用来for loop 比较 key 值是否相等的

使用pyhon试试 $hash $ 函数：

![image-20211113195530243](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211113195530243.png)





## **11.1 Direct-address tables**

>Direct addressing is a simple technique that works well when the universe U of keys is reasonably small.

直接寻址法 适用于key比较少的时候。



![image-20211112175349616](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211112175349616.png)



这样的方法同时记住了 key 和 data（而不是data的address） ，非常占用空间；



## **11.2 Hash tables**



Python用久了让人有 dict 很简单的错觉，所以这个内容让我思考了很久。

建议先看一下下文：

https://zhuanlan.zhihu.com/p/74003719



>With direct addressing, an element with key k is stored in slot k. 
>
>
>
>With hashing, this element is stored in slot **h(k)**; that is, we use a **hash function** h to compute the
>
>slot from the key k. 
>
>
>
>Here, h maps the universe U of keys into the slots of a **hash**
>
>**table** T[0 .. m-1]:
>
>
>
>h: U --->  {0,1, ... , m-1}



简而言之：

> **An element with key k hashes to slot h(k);**

hash function减少了indices的范围；



![image-20211112211617834](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211112211617834.png)



但是有时候两个key会被match到一个slot里面；这就是一个 **collision**; 参考上图。

比如我们的 ```hash(x) = x%10```, 这样的话25 和 35就会被match到同一个slot上，这就是一个冲突；



发生冲突并不可怕，有一些有效的方法能化解冲突带来的结果；（冲突本身是不可能解决的）



哈希算法最重要的特点就是：

- 相同的输入一定得到相同的输出；
- 不同的输入大概率得到不同的输出。



下面介绍原书中提供的最简单的冲突解决方法；

**1. Chaining:**

![image-20211112214633488](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211112214633488.png)

让每一个key都对应一个linked list;

一个例子：

![Lightbox](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/hashChaining1.png)

**2. 开放寻址法(open addressing):**



## **11.3 Hash functions**

**什么是好的 hash function?**

- **simple uniform hashing:** each key is equally likely to hash to any of the m slots

如果完全随机的插入slot, 就可以满足这个条件；

- 



Most hash functions assume that the universe of keys is the set N= {0,1,2, ......}

of natural numbers. Thus, if the keys are not natural numbers, we find a way to

interpret them as natural numbers.



比如最简单的**division method**:
$$
h(k) = k \mod m
$$





## 11.5 **Perfect hashing**

> A hashing technique **perfect hashing** if $O(1)$memory accesses are required to perform a search in the **worst** case.



为了做到完美哈希，第一个因素和之前的方法是一样的：选择一个好的 hash function $ h $ 把 $n$ 个 $keys$ hash into $m$ slots。



之后，除了使用chaining 搭建新 linked list的方法之外，转而使用一个小的第二哈希表 **secondary hash table $S_j$** ; 可以保证在**第二哈希level没有冲突**。



> **Theorem： **
>
> Suppose that we store n keys in a hash table of size $m = n^2$ using a hash function $h$ randomly chosen from a universal class of hash functions. 
>
> Then, the probability is less than $1/2$ that there are any collisions.
>
> 翻译：
>
> 使用随意一个哈希函数 $h$ ,把 n 个keys存到 $m = n^2$ 个slot里，有冲突的概率小于$1/2$



![image-20211113195124517](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211113195124517.png)

## 11.6 自己实现hashmap for string/text

题目来自Homework 8

>**Implement a hash for text.** 



>Given a string as input, construct a hash with words as keys, and wordcounts as values. Your implementation should include:
>
>•  a hash function that has good properties for text
>
>•  storage and collision management using linked lists
>
>•  operations: insert(key,value), delete(key), increase(key), find(key), list-all-keys





先来找一个适合string的hash func，google了以后：

http://www.cse.yorku.ca/~oz/hash.html



实施 $djb2$.

复习一下：

>Python 
>
>```ord```:
>
>输入一个字符，返回ASCII数值
>
>```hex```：
>
>输入整数，返回16进制



**实施hash_djb2:**

忘记位运算的先复习一下；

```python
def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF
```



这个函数的magic在于他的两个魔法数字：33和5381，这里用的是5381；这是一个经验主义得到的magic number,不用纠结太多；



贴一点test case:

```python
print(hash_djb2(u'hello world')) # '0xa6bd702fL'
print(hash_djb2('a'))
print(hash_djb2('b'))

#输出：
894552257
177670
177671
```



### Hash table python implementation

python自己实现哈希表



目标如下：

- 给定一段长文本txt文件，我的hashmap读入文件，以word作为key，word count作为value；

- 使用chaining 方法来handle collision



结果是这样的：

![image-20211202023112513](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211202023112513.png)



# 12 SkipList

![image-20211114201725611](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211114201725611.png)

跳表在工业中也会被经常用到，墙裂建议阅读下文：

https://www.jianshu.com/p/9d8296562806



简单概括重点：



**跳表的索引高度 $h = log_2n$，且每层索引最多遍历 3 个元素。所以跳表中查找一个元素的时间复杂度为 $O(3*logn)$，即：$O(logn)$。**



假如原始链表包含 n 个元素，则一级索引元素个数为 n/2、二级索引元素个数为 n/4、三级索引元素个数为 n/8 以此类推。所以，索引节点的总和是：n/2 + n/4 + n/8 + … + 8 + 4 + 2 = n-2，**空间复杂度是 O(n)**。



**为什么Redis选择使用跳表而不是红黑树来实现有序集合？**



Redis 中的有序集合(zset) 支持的操作：

1. 插入一个元素
2. 删除一个元素
3. 查找一个元素
4. 有序输出所有元素
5. 按照范围区间查找元素（比如查找值在 [100, 356] 之间的数据）

其中，前四个操作红黑树也可以完成，且时间复杂度跟跳表是一样的。但是，按照区间来查找数据这个操作，红黑树的效率没有跳表高。按照区间查找数据时，跳表可以做到 O(logn) 的时间复杂度定位区间的起点，然后在原始链表中顺序往后遍历就可以了，非常高效。



## skiplists实现详解

**跳表Skiplist的Python实现。**



https://leetcode.com/problems/design-skiplist/discuss/?currentPage=1&orderBy=most_votes&query=

Python:

这个实现是我从leetcode某个大哥那抄过来的，有做改动；



It really took me one day to understand....



```python
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.down = None
```

![image-20211115124703901](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115124703901.png)

```next``` 指的是**相同级别**的下一个元素，就是往右走；

```down``` 指的是**下一个级别**的相同元素，就是往下走；



**初始化：**

```python
class Skiplist:
    def __init__(self):
        self.levels = []
        self.max_level = 4
        prev = None
        for i in range(self.max_level):
            node = Node(-math.inf)
            self.levels.append(node)
            if prev:
                prev.down = node
            prev = node
```

在这次的实现中，levels储存的是每个级别的单链表。

index = 0 的位置存的是**最高级**的链表，我们在这一级别实现skip 操作；

index = 3 存的是最基础的链表，也就是长度为 $n$ 的链表，如下图：

> 后面统一一下口径，**最高级**的链表指 **index = 0**, 元素最少的那一条链表；

![image-20211115125047323](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115125047323.png)

通过上述代码，你实现了如下的操作：

1. ```self.level``` 中储存了每个级别的对应的链表, 每个级别链表的初始化都为负无穷：```-math.inf```
2. 让每个更高级的链表对象指向更基础的级别；



如图：

![image-20211115130101785](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115130101785.png)

**实现iter**

```python
    def _iter(self, val):
        res = []
        l = self.levels[0]
        while l:
            while l.next and l.next.val < val:
                l = l.next
            res.append(l)
            l = l.down
        return res
```

这个函数是很核心的函数，后面的操作都会用到它；

这个函数**实现了skip**的作用：



- **输入一个```val```, 只要下一个元素比```val```小，就往右走(```next```)；**

- **否则，就往下走(```down```)；**



为什么是```while l```,因为他只能往右或者往下走，就一定有走到None的时候；



所以，这个函数中返回的结果```res```是**每个级别**中刚好小于```val```的那个node节点对象；

**即使下一个元素能等于val, 也停留在之前一个，方便后续delete操作**；



这个函数实现了，理解了返回的res是什么，后续就简单了；



**search 搜索操作：**

```python
    def search(self, target: int) -> bool:        last = self._iter(target)[-1]        return last.next and last.next.val == target
```



上一个```_iter```函数停留在输入值的前一个数，所以直接检查下一个元素就好了；



**add/insert**操作

```python
    def add(self, num: int) -> None:        res = self._iter(num)        prev = None        for i in range(len(res) - 1, -1, -1):            node = Node(num)            #res[i]是刚好比val小的元素，那么next就比val大咯            node.next = res[i].next            #指向低级链表            node.down = prev            #res[i]是刚好比val小的元素            res[i].next = node            prev = node            rand = random.random()            if rand > 0.5:                break
```



- 这个```for```是从低级走到高级的
- 在保证了基础级别存在插入的数值以后，每个更高级的节点都```random```一次，大于0.5就在更高级的节点添加该节点；

**erase/delete删除操作**

有了```_iter```操作后很简单，不用说了



# 13 红黑树：Red-Black Trees

先仔细阅读下原文：

>A **red-black tree** is a binary search tree with one extra bit of storage per node: its
>
>**color**, which can be either RED or BLACK. By constraining the node colors on any
>
>simple path from the root to a leaf, red-black trees ensure that no such path is more
>
>than twice as long as any other, so that the tree is approximately **balanced**.
>
>
>
>Each node of the tree now contains the attributes ```color```, ```key```, ```left```, ```right```, and ```p```.



![image-20211115142150384](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115142150384.png)

**所以红黑树本质就是自平衡的BST，但是他多了颜色属性，并且服从红黑树性质:** 



```
1）每个结点要么是红的，要么是黑的。  2）根结点是黑的。  3）每个叶结点（叶结点即指树尾端NIL指针或NULL结点）是黑的。  4）如果一个结点是红的，那么它的俩个儿子都是黑的。  5）对于任一结点而言，其到叶结点树尾端NIL指针的每一条路径都包含相同数目的黑结点。  
```



**红黑树的查找、插入、删除的时间复杂度最坏为O(log n)。**



![image-20211115142406698](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115142406698.png)



如果忘记了BST的性质，先去上面复习一下 Insertion 和 Deletion 的操作。



## 13.1. Rotation

>When we do a left rotation on a node x, we assume that its right child y is not T:nil; x may be any node
>
>in the tree whose right child is not T:nil. The left rotation “pivots” around the link
>
>from x to y. It makes y the new root of the subtree, with x as y’s left child and y’s
>
>left child as x’s right child.



我们要**左**旋节点某子树的根节点： ```x```;

假设``x`` 的右child ``y``的 不为空：

​		旋转围绕着 ``x``和``y``的连接，我们让：

				- ``y``成为该子树的root, 			- ``x``成为 ``y`` 的左child, ``y`` 原来的左child成为 ``x``的右child。



![image-20211115214746244](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115214746244.png)

​																		figure 来自原文**13.2** *p313*



伪码：

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115215706930.png" alt="image-20211115215706930" style="zoom:80%;" />



左旋、右旋的时间复杂度为**$O(1)$**。



## 13.2. Insertion

插入的时间复杂度为 $O(lg n)$



![image-20211115225148522](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115225148522.png)



为了保证红黑树性质，需要一个额外的``fix``函数来 recolor 以及 rotate

![image-20211115231701130](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115231701130.png)

今天被旋晕了，下次再来吧



**Case 1:** ``z's`` uncle ``y`` **is red**

**Case 2:** **z’s uncle** y **is black and** z **is a right child**

**Case 3:** **z’s uncle** y **is black and** z **is a left child**



总共有6个cases;

因为3个3个cases之间是对称的，因此

我们关注三个case:

> **Case 1:** ``z's`` uncle ``y`` **is red**
>
> **Case 2:** **z’s uncle** y **is black and** z **is a right child**
>
> **Case 3:** **z’s uncle** y **is black and** z **is a left child**



**Case 1:** ``z's`` uncle ``y`` **is red**

z的舅舅是红色的，此时违反了性质4: 即一个red的儿子必须是两个black;



![image-20211126002114594](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211126002114594.png)

此时的操作：

```
1. 把uncle由红变黑；2. 把parent(A)变黑3. 把爷爷(c)变红；4. 把指针从z移到爷爷
```



**Case 2:** **z’s uncle** y **is black and** z **is a right child**

case 2和 case 3是相互交织的；

case 2还是违反了性质4；此时用一个**左旋**/**右旋**直接进入case 3;



![image-20211126003149715](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211126003149715.png)

```
1.移动指针到parent2.旋转，进入case3
```



**Case 3:** **z’s uncle** y **is black and** z **is a left child**

```
1.翻转parent和爷爷的color;2.对爷爷调用旋转；
```



**插入以后会导致RBT的那些性质会被violated?**

- Property 2: 根节点是黑

当树为空时，插入的节点是红色的，这时违反；

- Property 4: 红色节点不能有红色节点，只能有两个黑色节点；（NIL也算黑色）



![image-20211115232733643](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115232733643.png)



## 13.3. Deletion





## 13.4. Why Red-Black-Tree?

https://www.quora.com/Difference-between-binary-search-tree-and-red-black-tree

一开始没理解R-B-Tree 比 BST强的地方，谷歌了一下总结如下：

常规的BST不是self-balancing的，因此你的**插入顺序**会导致其他操作的时间复杂度发生变化；

比如：

- if you inserted in order {2, 3, 1}, the BST will be O( log(N) )
- however if you inserted {1,2,3}, the BST will be O( N ), like a linked list.



而RB-Tree总能自平衡，来确保你的操作总会是$O(lgn)$。

**Red Black Tree : best case O(logN), worst case O(logN)**
**Binary Search Tree: best case O(logN), worst case O(N)**



# 17 Amortized Analysis: 平摊分析

在平摊分析中，执行一系列数据结构操作所需要的时间是通过执行的所有操作求平均而得出的。

## 17.1. Aggregate analysis

如果堆栈添加一个新的操作```MULTIPOP``` 来一次性弹出栈顶的 $n$ 个元素：

```
PUSH(S, x):将x压入S
POP（S）：弹出栈顶
MULTIPOP（S, k）：弹出栈顶k个对象
```



在最坏情况下，MULTIPOP操作的时间复杂度为O(n)。



现在开始分析由*n*个*PUSH*， *POP*和*MULTIPOP*操作序列，其作用于一个初始为空的栈：



每个操作的最坏情况是$O(n)$, 因此n个操作序列的代价是$O(n^2)$;



这一分析虽然正确，但是这个bound不够紧凑；



一个对象在每次被压入栈后，至多被弹出一次。所以，调用POP（包括MULTIPOP）的次数至多等于PUSH的次数，即至多为n.。对任意的n，包含n个PUSH, POP, MULTIPOP操作的序列的总时间为O(n). 每个操作的平均代价为O(n) / n = O(1).。 



**聚集分析中，将每个操作的平摊代价指派为平均代价。所以三个栈操作的平摊代价都是O(1)。**



## 17.2. Accounting methoed: 记账法

**直觉是这样的：Accounting Method，要求你先计算出每个操作要“存”多少钱，然后给别的操作消费。**



在平摊分析的记帐方法中，对不同的操作赋予不同的费用，某些操作的费用比它们的实际代价或多或少。



我们对一个操作的收费的数量称为平摊代价。当一个操作的平摊代价超过了它的实际代价时，两者的差值就被当作存款(credit)，并赋予数据结构中的一些特定对象，可以用来补偿那些平摊代价低于其实际代价的操作。

数据结构中存储的总存款等于总的平摊代价和总的实际代价之差。注意：总存款不能是负的。



**核心思想是PAY IN ADVANCE：提前支付费用**



**Stack Operations**

| **操作** | 真实花费 | 平摊花费 |
| -------- | -------- | :------- |
| Push     | 1        | 2        |
| Pop      | 1        | 0        |
| MultiPop | min(k,s) | 0        |

可以看到对于Push操作，平摊花费比真实花费要多1，这个1即使`credit`。即栈中的每个元素都有一个值为1的credit，之后的Pop操作和Multipop操作平摊花费都为0，相当于是使用一个`credit`。因为在Pop前都必须调用了相应数量的Push，所以总和的`credit`永远不会小于0

因此对于一系列n个操作而言，其总共的平摊花费也是O(n)。



## 17.3. Potential Method: 势能法

原文：

![image-20211121182905800](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121182905800.png)



我们假设数据结构$Di−1$在进行了第$i$个操作后，变为了数据结构$Di$，其中第i个操作的真实花费为$ci$，数据$Di$的势能为$Φ(Di)$，数据$Di−1$的势能为$Φ(Di−1)$。在使用势能法时，平摊开销(amortized cost)就是：

![image-20211121183511698](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121183511698.png)

平摊开销 =  真实开销 + 势能差 （核心思想和上一节的acounting 方法一样，把“提前支付”变成了储存势能 -> 释放势能）



经过 $n$次操作以后, 平摊开销就是：

![image-20211121184240125](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121184240125.png)



继续使用stack作为例子：

我们定义potential function $Φ$ 是stack的数据数量；

那么对于空栈$D_0$来，他的$Φ(D_0)$就是0；



如果第$i$次的操作是对一个 *长度为 $s$的堆栈 $D_0$* 进行**PUSH**操作，那么势能差：

![image-20211121185201293](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121185201293.png)



求出平摊开销：

![image-20211121185224518](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121185224518.png)



如果第 $i$ 次的操作是**MULTIPOP**操作，我们要将![image-20211121185856165](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121185856165.png) 个数据对象全部pop出去，那么势能差为：



![image-20211121185931885](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121185931885.png)

平摊开销：

![image-20211121185948220](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211121185948220.png)

好文：帮助理解

https://www.zhihu.com/question/40156083



# 19 Fibonacci Heaps: 斐波那契堆

这算法看的比红黑树还眩晕，细节参考原文吧，网上教程也很少；

![image-20211122234213923](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211122234213923.png)

- 一组满足堆性质（一般是**最小堆**性质）的**树**的集合
- 始终保持一个指针指向最小的元素的对象
- 使用```marked```node属性，来保持heaps的扁平







**Mergeable Heaps: 可和并堆**:

定义：

>可合并堆支持以下五个操作，并且每一个元素都有一个```key```:
>
>![image-20211122132217137](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211122132217137.png)
>
>
>
>Fibonacci 堆额外支持以下两个操作：
>
>![image-20211122132302820](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211122132302820.png)
>
>
>
>操作的时间复杂度如下：
>
>![image-20211122132428819](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211122132428819.png)



## 19.1. Structure of Fibonacci heaps

![image-20211206011340536](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206011340536.png)

最重要的第一句话就是：

>A **Fibonacci heap** is a collection of rooted trees that are **min-heap ordered**. That
>
>is, each tree obeys the **min-heap property**:

即：

1. **斐波那契堆是树的集合，每一棵树都满足最小堆性质；**

就像是$[root1,root2, ..., rootN]$, 每个root都是一个树；他们彼此之间用**Double Linked List**串起来;



2. **Fib Heap**的特点是始终维护一个指针指向最小值的节点；



3. root的每一个node $x$ 都有 ```x.p```指向parent, ```x.child```指向一个children;

x的children用**双向链表** 像环一样的连在一起，我们叫他```child list of x```



>![ ](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211122134407345.png)
>
>



看伪码会看傻逼的，我总结一下几个操作：





## ```insert```: 斐波那契堆的插入操作



![image-20211206020839193](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206020839193.png)

![image-20211206020920535](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206020920535.png)

注意：

- 我们直接插入root list而不是某个节点的child list

  

![image-20211206021133020](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206021133020.png)

**合并两个堆，这个操作比较简单，核心就是直接concatenate两个堆的root list, 更新min指针；**





## ```extract_min()```: 最复杂的操作

这个操作会像pop出当前最小的节点，然后调用```consolidate```来确保自己的结构不被破坏；

*这是最核心的操作，也是最眩晕的操作：*

![image-20211206021312030](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206021312030.png)

- 根据```min```指针取出最小对象，say ```z```；
- 如果```z```有child, 把所有child先**升级到root list**当中，然后将parent设置为**None**；
- 设置好各种left 和 right指针，把```z```移除；
- 判断：
  - 如果```z```是唯一节点，那么成了空堆，把min指针和root list都设置为None
  - 很可惜他往往不是唯一节点，那么就要调用```consolidate```方法

- 最后将树的节点数-1



```consolidate```:

```degree```的作用在这个函数体现，**我们要确定每个node的```degree```都是不同的**;



- 遍历root list的节点：
  - 如果degree相同，把值小的节点从从root list中拿掉，连接到值大的节点的child方法上；这个操作是用```heap-link```函数来实现的；之后，把值更大的节点的degree + 1

经过这个操作以后，堆结构会变得更加扁平；



关于decrease key操作，降低某个节点的值，所以可能破坏最小堆性质；

因此又是一堆伪码；上张图理解一下intuition吧：



![image-20211123013817471](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211123013817471.png)





# 22 Graph: 图

BFS/DFS: $O(E+V)$

Topological sort: $O(V+E)$

## 22.1 图的表示：

表示图的标准方法：
$$
G = (V,E)
$$
Graph是由Vertices定点和Edges边组成的；

**无向图**有两种表示法: 

![image-20211127191038926](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211127191038926.png)



(a): 由5个顶点，7个边组成的无向图

**(b): list表示法(adjaceny-list representation) of G**

**(c): matrix表示法(The adjacency-matrix representation) of G**

再无向图中，(c)是对称的;



**有向图(directed graph)**表示法类似：

![image-20211127191524068](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211127191524068.png)

(a):由6个顶点，8个边组成的无向图

**(b): list表示法(adjaceny-list representation) of G**

**(c): matrix表示法(The adjacency-matrix representation) of G**





## 22.2 BFS：广度优先搜索

广度优先搜索，没啥说的了；



![image-20211209220724891](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209220724891.png)



这里color = white代表没遇到过的节点；

d表示距离；

$\pi$ : 代表parent;

这里使用堆栈的方法来储存接下来要开始BFS的节点；



RUNTIME: $O(V+E)$

## 22.3 DFS： 深度优先搜索





![image-20211128015820198](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211128015820198.png)



**请注意开始和结束的时间，使用DFS来计算终止时间的方法会在后续算法被用到。**

![image-20211128020036926](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211128020036926.png)



## 22.4 DAG & Topological Sort: 有向无环图 与 拓扑排序

**DAG（Directed acyclic graph）有向无环图**:

无法形成cycle就是DAG，最后一定会终止在某个点；

![image-20211204211614482](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211204211614482.png)

严格的定义如下：





因为这样的特性，才能被拓扑排序;

**拓扑排序 (Topological Sort)：**



![image-20211209225116837](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209225116837.png)

RUNTIME: $O(V+E)$



## 22.5 Strongly connected components

啥是紧密连接组件？看图就懂了：



![image-20211210000159590](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211210000159590.png)

严格定义如下：

Strongly connected component of a directed graph $G = (V,E)$ is a maximal set of vertices $C \in V$ such that for every pair of vertices $u$ and $v$ in $C$, **we have both u~\>v and v~>u;** that is, **vertices u and** 

**v are reachable from each other.**



使用DFS来发现紧密组件：

![image-20211210000521341](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211210000521341.png)





## 23. 最小生成树: Minimum Spanning Trees

Spanning Trees:



**A set of edges A that “span” or “touch” all vertices, and forms no cycles**



最小生成树往往是在**无向有权图**上来讨论。

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211129225540791.png" alt="image-20211129225540791" style="zoom:67%;" />

最小生成树不一定是唯一的；



**简单的定义：你希望找到一组边：1.连接了所有点 2. 总权重最小**



严格定义如下：

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211129225642221.png" alt="image-20211129225642221" style="zoom: 80%;" />



找到最小生成树的算法的大致**模糊思路**如下，详细的会在下一节展，这里看看就好：

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211129230119205.png" alt="image-20211129230119205" style="zoom:80%;" />

A是一组边的集合，一开始设为空集，最终会成为一颗MST（最小生成树）;

如图，在A成为完整MST前，每一步我们都：

- 找到一条 "safe edge", 并加入A

知道A成为完整MST。



因此，核心就是如何判断edge是不是safe的。

how to find a safe edge to a given set of edges A? 

- Prim algorithm 
-  Kruskal algorithm

在展开算法前，对一些术语下定义：



先给原文，再给我的简单理解：

<img src="https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211129230716056.png" alt="image-20211129230716056" style="zoom:80%;" />

1. **图的切分：cut(S, V - S)**

**cut(S, V - S)**；

很直观，切分后S代表黑点；V-S是白点，下方；



2. 如果一条边在S和V-S各有一个顶点，那我们说这条边**cross** cut(S, V - S)



3. 在cross的边中，weight最小的边叫做**light edge**.

![image-20211129235123255](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211129235123255.png)



## 23.2 最小生成树算法: The algorithms of Kruskal and Prim

两个算法都是贪心算法。

### Kruskal's Algorithm



![image-20211130010445278](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211130010445278.png)

> **1.** *Sort all the edges in non-decreasing order of their weight.* 
> **2.** *Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If cycle is not formed, include this edge. Else, discard it.* 
> **3.** *Repeat step#2 until there are (V-1) edges in the spanning tree.*





第六行的```find-set```操作其实就是检查图是否有形成cycle。

所以，核心就是将边先按照**升序**排序，然后进行遍历；

因此每次都是当前最小权重的edge。

对当前遍历到的边：

- 如果加入这条边后，形成了cycle, 那么跳过这条边；
- 反之，没有形成cycle，那么将当前的边加入A

最后返回。

![image-20211130011503449](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211130011503449.png)

![image-20211130012241595](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211130012241595.png)



一个简单的并查集算法:

```python
# Python Program for union-find algorithm to detect cycle in a undirected graph
# we have one egde for any two vertex i.e 1-2 is either 1-2 or 2-1 but not both

from collections import defaultdict


# This class represents a undirected graph using adjacency list representation
class Graph:

    def __init__(self, num_of_vertices):
        self.V = num_of_vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A utility function to find the subset of an element i
    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        if parent[i] != -1:
            return self.find_parent(parent, parent[i])

    # A utility function to do union of two subsets
    def union(self, parent, x, y):
        parent[x] = y

    # The main function to check whether a given graph
    # contains cycle or not
    def isCyclic(self):

        parent = [-1] * (self.V)

        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for i in self.graph:
            for j in self.graph[i]:
                x = self.find_parent(parent, i)
                y = self.find_parent(parent, j)
                if x == y:
                    return True
                self.union(parent, x, y)


# Create a graph given in the above diagram
g = Graph(3)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 0)

if g.isCyclic():
    print("Graph contains cycle")
else:
    print("Graph does not contain cycle ")

# This code is contributed by Neelam Yadav

```





### Prim's Algorithm





## 24. Single Source Shortest Paths: 最短路径问题

![image-20211203212607552](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211203212607552.png)



**Big name Algorithm:**

- Dijkstra algorithm

- Floyd Warshall algorithm

### 定义问题：



本章节关注**单源头**(single source)最短路径问题：给定图 $G(V,E)$ ,找到一个**给定的点** $s$ 到**图中所有点**的最短路径。



### **负权重边的影响**



![image-20211204000219107](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211204000219107.png)



- $s - b$ 只有一条路径，此时负权重边无影响；
- $s - d$ 有无限条路径：$<s,c>, <s,c,d,c>,<s,c,d,c,d,c>$, 但是最小权值路径还是$<s,c>$,因此也不受影响；
- 关于 $s-e$, 同样有无限路径：$<s,e>, <s,e,f,e>,<s,e,f,e,f,e>$, 但是 $<e,f,e>$ 的权重是$3 + (-6) = -3 < 0$, 因此 $<s,e>$ **没有最短路径；**因此我们表示$<s,e> = -\infty$ ;
- $<s,g>$,**因为$g$和$f$是相连的**，因此$<s,g>$**也没有最短路径**；$<s,e> = -\infty$ ;
- $s$ 永远无法抵达 $h, i, j$ ,所以$<s,h> = <s,i> = <s,j> =  \infty$ 



**Dijkstra算法** 假设所有边都是**非负数**；

**Bellman-Fordrm 算法** 没有这种假设；



### Relaxation: 更新最短路径的机制

good explanation from :

https://stackoverflow.com/questions/2592769/what-is-the-relaxation-condition-in-graph-theory



- You have two nodes, `u` and `v`
- For every node, you have a *tentative distance* from the source node (for all nodes except for the source, it starts at positive infinity and it only decreases up to reaching its minimum).

**你使用relaxation来检测是否能improve到达某个节点的shortest path。(每个节点初始值默认为无穷大)**

举个例子：

```
s ~~~~~~~> v
 \         ^
  \        |
   \~~~~~> u
```





比如上图，s是源点，那么:

- 目前**已知**从s出发能到达v, 我们表示为distance(s,v)
- 你也知道s能到u, 表示为distance(s,u)

在使用Relaxation的某个算法的某个时刻遍历到$<u,v>$ 这条边，就会判断：If `dist[u] + weight(u, v) < dist[v]`, 那么 `s~>u->v` is shorter than `s~>v`, 所以我们应该更新s - v的最短路径！



理解这个很重要，后面直接用Relax来表示这个机制；

### BELLMAN-FORD算法

初始化一个长度是 $V$ 的矩阵 $[ 0,\infty,\infty,... ]$，代表源头到其他点的距离，第一项设为0因为是自己到自己的距离；

之后就是Relaxation: 像DP 一样不断更新$s$ 到其他点的最短路径；

<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gx2hsbtja6j31420gsn0h.jpg" alt="image-20211204161009003" style="zoom: 50%;" />



<img src="https://tva1.sinaimg.cn/large/008i3skNgy1gx2ht4kpqnj312x0u0q7m.jpg" alt="image-20211204161054751" style="zoom:50%;" />





```
      2
V0-----------V1
 \            \
4 \            \ 5
   \            \
   V2------------V3
          2
```



书上例子不太好，用这个走一遍：



- 1. 初始化$dist = [0, inf, inf, inf]$

- 2. 走到边$<v0 - v1>$ , $dist[0] + 2 < dist[1]$ 成立, 更新$dist = [0, 2, inf, inf]$
- 3. 走到边$<v0 - v2>$ , $dist[0] + 4 < dist[2]$ 成立, 更新$dist = [0, 2, 4, inf]$

- 4. 走到边$<v1 - v3>$ , $dist[1] + 5 < dist[3]$ 成立, 更新$dist = [0, 2, 4, 7]$
- 5. 走到边$<v2 - v3>$ , $dist[2] + 2 < dist[3] = 7$ 成立, 更新$dist = [0, 2, 4, 6]$



这是第一遍，**我们总共要走**$V-1$**遍才能结束**，但是后面的两遍都不会有更新了；



为啥要走$V-1$遍呢？目前我发现和**储存顺序有关**；

再来一个例子：

![image-20211204200430160](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211204200430160.png)



如果你按照顺序 1-2, 2-3, 3-4来储存，可以一遍过；

但是如果是3-4, 2-3, 1-2，你需要$V-1$ 也就是三次才能走对；

因为如果当前节点之前没遇到过，$dist[当前节点]$就是$\infty$, 无法被更新；

在程序里会判断**每一步**的出发点是否是NIL; 可以去代码试一下；





### 24.2 DAG shortest path: DAG的最短路径

657

对拓扑排序好的DAG，按照顺序用一遍RELAX即可：

![image-20211204204831258](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211204204831258.png)



RUNTIME: $ O(V+E) $



### 24.3 Dijkstra 算法



Dijkstra算法比Bellman-ford更快，但是需要图中不存在负循环；

![image-20211204222435609](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211204222435609.png)



- 2,3行的 $S$ 代表最短路径集合，而 $Q$ 是没探索的点，也就是 $V-S$，一开始就是所有点$G.V$; Q是用最小优先队列(堆算法)实现的，有 ``` EXTRACT-MEAN ```方法；还需要 ```MIN-HEAPIFY``` 方法；

只要 $Q$ 不空就循环：

- 从Q



## 25 All-Pairs Shortest Paths



>In this chapter, we consider the problem of fifinding shortest paths between all pairs
>
>of vertices in a graph. 



上一张是sinle source shortest path (SSSP)，求出源点到其他所有点的最短距离;

本章节关注**All-Pairs Shortest Paths** (APSP), 求出所有点之间的最短距离。



### 25.1 Matrix Multiplication算法

使用DP的方法不断更新最小路径；

回顾一下矩阵A 乘以 矩阵B的是matrix multiplycation算法：

![image-20211205235342182](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211205235342182.png)

APSP图算法和这个极为相似：

![image-20211205235430503](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211205235430503.png)

时间复杂度是$O(n^3)$

解释一下 $l_{ij}^m$ :

$l_{ij}^m$ 代表了： 在最多$m$ 条边的情况下, 点$i$ 到 点$j$ 的最小weight. 因此：



![image-20211205235903734](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211205235903734.png)



如果m大于1:

![](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206000442309.png):

这里是DP的思想，遍历所有中介点k来尝试更新 $i$ 到 $j$ 能不能有更短的距离；*(原书的版本写的实在太绕了，希望我的总结能帮你get到 intuition :) )* 



总体的APSP算法如下：

![image-20211206001006615](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206001006615.png)

总耗时$O(n^4)$.



总体思想如下：

![image-20211206001420174](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206001420174.png)



这是一个Bottom up的算法，随着m的增加，我们不断更新L矩阵；到最后m = n-1,就得到了全局的最小权重路径；

这个算法又绕又慢，不看也罢；



### 25.2 The Floyd-Warshall algorithm

时间复杂度：$O(V^3)$

简单粗暴多了(可以直接看下面的改进版，忽略这个)

![image-20211206001835830](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206001835830.png)

改进版：

W是矩阵表示法的图，输入进去：

这个算法我们只需要维护一个矩阵，减少了空间占用；

![image-20211206002127309](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211206002127309.png)

一句话概括就是在所有$i$ 到 $j$ 的中间再遍历一层 $k$, 使用DP方法动态更新 $i$ 到 $j$ 的最短路径；



顺便贴一下leetcode:[https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/]







## 26 Maximum Flow：最大流问题

**Flow networks**

> A flow network $G = (V,E)$ is a directed graph in which each edge $(u,v) \in E$ has a nonnegative capacity $c(u,v) \geq 0$.

**Flow networks**是有向图，每一条边多了一个运载能力(capacity),代表通过这条边的上线；(想象网络负载的场景)



在这一章我们主要关注 Maximum flow problem:



>  In maximum flow problem, we are given a flow network G with **source s and sink t**, and we wish to find a flflow of maximum value.



这里又引入了两个概念：source 和 Sink



## 26.2 The Ford-Fulkerson method

We call it a “method” rather than an “algorithm” because it encompasses

several implementations with differing running times. 

![image-20211209134842153](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209134842153.png)



为了理解这个算法，引入残差网络的概念：

###  Residual networks

![image-20211209174916280](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209174916280.png)



augmentation

![image-20211209175126666](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209175126666.png)



![image-20211209175811719]()

![](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209175811719.png)









![image-20211209183355749](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211209183355749.png)





























# 位运算算法

**原码**

是一种计算机中对数字的二进制定点表示方法。原码表示法在数值前面增加了一位符号位（即最高位为符号位）：正数该位为0，负数该位为1（0有两种表示：+0和-0），其余位表示数值的大小。



![image-20211118215529377](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211118215529377.png)



缺点：

- 原码中的0分为`+0`和`-0`

- 在进行不同符号的加法运算或者同符号的减法运算时，不能直接判断出结果的正负，我们必须要将两个值的绝对值进行比较。然后再进行加减操作。



**反码**

正数的反码就是原码：

![image-20211118215852263](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211118215852263.png)



**补码**

在计算机系统中，数值一律用[补码](https://baike.baidu.com/item/补码)来表示和存储。

原因在于，使用补码，可以将符号位和数值域统一处理；同时，加法和减法也可以统一处理。此外，补码与原码相互转换，其运算过程是相同的，不需要额外的硬件电路支持。

记住口诀：正数的补码与原码相同，负数的补码为其原码除符号位外所有位取反（这就是反码了），然后最低位加1。

![image-20211118220439000](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211118220439000.png)



### **如何check if 一个数是2的次方？**

方法1：

如果数字能不停被2整除，并且最终等于1，那么是2的次方；

否则不是。

这个方法的时间复杂度是$O(lgn)$

```python
def isPowerOfTwo(n):    if (n == 0):        return False    while (n != 1):            if (n % 2 != 0):                return False            n = n // 2                 return True
```





方法2：

使用位运算。



如果一个数是2的次方，那么位运算：```n & (n - 1)```结果必定是0。（只要n > 0）



为啥呢？



2, 4, 8, 16 .... 这样的2的次方的数字的二进制数都只有第一位是1；

只要把他们减一，比如：

把4 - 1 = 3 –> 011 
  16 - 1 = 15 –> 01111

而4 = 100

16 = 10000,



这样如果进行```&```运算，就不会有任何一位相等；4&3 == 0， 16&15 == 0；



所以我们的函数：

```python
def isPowerOfTwo(x):	return (x and (not(x & (x - 1))))
```



### 二进制数中 1 的数量

首先, python中有内置函数，来count1:

```python
>>> bin(5)'0b101'>>> bin(5).count('1')2
```

但是这不是我们想要的。



玩的就是old school:



继续上一个算法 ，每次一个数字n被减去 1, **最右边的1 和 再往右的数字就会被翻转；**



因此这个神奇的操作：



```python
n & (n - 1)
```



每次会让原来的数字中少一个1；(每次转掉一个1)



就这样用循环来count 1的数量即可；



以23 和 22 为例子：

23 ： 10111

22： 10110



23 & 22 = 10110 = 22

21: 10101

22 & 21 = 10100 = 20

19: 10011

20 & 19 = 10000 = 16

16 & 15 = 0



来一题LC：汉明距离：

https://leetcode.com/problems/hamming-distance/



```python
class Solution:    def hammingDistance(self, x: int, y: int) -> int:        x = x^y        res = 0         while x:            x = x & (x - 1)            res += 1        return res
```



先进性异位运算，在count("1")即可。













































































































# 额外的图LeetCode



![image-20211117142319656](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211117142319656.png)

```python
def bfs(n, m, edges, s):    queue = [s]    visited = [s]    dists = {s: 0}    adjList = {}    for i in range(len(edges)):        edge = edges[i]        x = edge[0]        y = edge[1]        if x in adjList:            if y not in adjList[x]:                adjList[x].append(y)        else:            adjList[x] = [y]        if y in adjList:            if x not in adjList[y]:                adjList[y].append(x)        else:            adjList[y] = [x]    while len(queue) > 0:        node = queue.pop(0)        if node in adjList:            neighbors = adjList[node]            for j in range(len(neighbors)):                if neighbors[j] not in visited:                    dists[neighbors[j]] = dists[node] + 6                    visited.append(neighbors[j])                    queue.append(neighbors[j])    res = []    for i in range(1,n+1):        if i not in dists:            res.append(-1)        elif dists[i] != 0:            res.append(dists[i])    return res
```









# 附录

![image-20211025160940605](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025160940605.png) 

egg_drop 

cd /d 
