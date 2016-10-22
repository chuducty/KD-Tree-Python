# KD-Tree-Python


1) (Optional) Run create_test.py to create inputkd.txt (input files) for testing. <br />
2) If you don't do step 1, delete all the lines below the VEB class. Those lines are for reading input files to test.

A Kd-tree (2d) written in python.
Support range query in O(sqrt(n+k)) (n is number of points, k is number of results)

## How to use Kd-tree.
**To use VEB, first,**
```
 k = KdTree()
 k.build(point_li)
 #point_li is the list of points
```


**To see how many points are there in an Area,**
```

 area = (min_x,max_x,min_y,max_y)
 print(k.query(area))
```
area is a rectangle with a form like this.
<img width="468" alt="screen shot 2016-10-22 at 10 28 49 pm" src="https://cloud.githubusercontent.com/assets/17826527/19619296/1838f442-98a7-11e6-8e23-c2c9ce4c2363.png">



## Running time of Kd-Tree.

<img width="470" alt="screen shot 2016-10-22 at 10 33 36 pm" src="https://cloud.githubusercontent.com/assets/17826527/19619316/9c0ba7c4-98a7-11e6-83c2-8d1edf2a95a3.png">

