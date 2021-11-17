# 1. Notes for Introduction to Algorithms

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
  - T(n) = O(n logn) means T(n) grows not faster than CONST*n*log(n)



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

## 6.3 Heap sort

### 6.3.1 MAX-HEAPIFY

最大堆性质：

 In a **max-heap**, the **max-heap property** is that for every node i other than the root:

![image-20211026155535675](C:/Users/Administrator/AppData/Roaming/Typora/typora-user-images/image-20211026155535675.png)



为了满足最大堆性质，你需要调用:

****:

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
> ***剩下的，交给递归recursive***
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
>>
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
>    The first approach is top-down with memoization. In this approach, we write the procedure recursively in a natural manner, but modifified to save the result of
>each subproblem (usually in an array or hash table). 
>    The procedure now first checks to see whether it has previously solved this subproblem. If so, it returns the saved value, saving further computation at this level; if not, the procedure computes the value in the usual manner. We say that the recursive procedure has been memoized;it “remembers” what results it has computed previously.
>
>
>
>The second approach is the **bottom-up method**. 
>
><details>
>    This approach typically depends on some natural notion of the “size” of a subproblem, such that solving any particular subproblem depends only on solving “smaller” subproblems. We sort the subproblems by size and solve them in size order, smallest first. 
>    When solving a particular subproblem, we have already solved all of the smaller subproblems its solution depends upon, and we have saved their solutions. We solve each subproblem only once, and when we first see it, we have already solved all of its prerequisite subproblems.  

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

Given a string as input, construct a hash with words as keys, and wordcounts as values. Your implementation should include:

•  a hash function that has good properties for text

•  storage and collision management using linked lists

•  operations: insert(key,value), delete(key), increase(key), find(key), list-all-keys



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



python 位运算：

按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：

下表中变量 a 为 60，b 为 13，二进制格式如下：

```
a = 0011 1100

b = 0000 1101

-----------------

a&b = 0000 1100

a|b = 0011 1101

a^b = 0011 0001

~a  = 1100 0011
```



实施hash_djb2:



```python
def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF
```

这个函数的magic在于他的两个魔法数字：33和5381，这里用的是5381；



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
    def search(self, target: int) -> bool:
        last = self._iter(target)[-1]
        return last.next and last.next.val == target
```



上一个```_iter```函数停留在输入值的前一个数，所以直接检查下一个元素就好了；



**add/insert**操作

```python
    def add(self, num: int) -> None:
        res = self._iter(num)
        prev = None
        for i in range(len(res) - 1, -1, -1):
            node = Node(num)
            #res[i]是刚好比val小的元素，那么next就比val大咯
            node.next = res[i].next
            #指向低级链表
            node.down = prev
            #res[i]是刚好比val小的元素
            res[i].next = node
            prev = node
            rand = random.random()
            if rand > 0.5:
                break
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
1）每个结点要么是红的，要么是黑的。  
2）根结点是黑的。  
3）每个叶结点（叶结点即指树尾端NIL指针或NULL结点）是黑的。  
4）如果一个结点是红的，那么它的俩个儿子都是黑的。  
5）对于任一结点而言，其到叶结点树尾端NIL指针的每一条路径都包含相同数目的黑结点。  
```



**红黑树的查找、插入、删除的时间复杂度最坏为O(log n)。**



![image-20211115142406698](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211115142406698.png)



如果忘记了BST的性质，先去上面复习一下 Insertion 和 Deletion 的操作。



## 13.1. Rotation

>When we do a left rotation on a node x, we assume that its right child y is not T:nil; x may be any node
>
> in the tree whose right child is not T:nil. The left rotation “pivots” around the link
>
>from x to y. It makes y the new root of the subtree, with x as y’s left child and y’s
>
>left child as x’s right child.



我们要**左**旋节点某子树的根节点： ```x```;

假设``x`` 的右child ``y``的 不为空：

​		旋转围绕着 ``x``和``y``的连接，我们让：

				- ``y``成为该子树的root, 
				- ``x``成为 ``y`` 的左child, ``y`` 原来的左child成为 ``x``的右child。



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

















# 附录

![image-20211025160940605](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211025160940605.png) 

egg_drop

