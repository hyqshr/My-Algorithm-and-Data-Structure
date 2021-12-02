# 12 SkipList 

- skiplist python

![image-20211114201725611](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/image-20211114201725611.png)

跳表在工业中也会被经常用到，墙裂建议阅读下文：

https://www.jianshu.com/p/9d8296562806



简单概括重点：



通过多级索引加速查找；

![img](https://raw.githubusercontent.com/hyqshr/MD_picgo/main/19063731-3852cc36af701f46.jpeg)

比如要查找10这个元素，我们从高级索引开始查找，停在比10小的高级索引之前，也就是7，然后往下级查找，以此类推；这样加速查找流程。



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