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




## Running time of Kd-Tree.


