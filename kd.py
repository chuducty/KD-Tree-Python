import random
import string
import time
import math
def kselect(li,k):
    
    while True:
        r = random.randint(0,len(li)-1) # random a number
        cur = li[r]
        #swap to the first element
        tmp = li[0]
        li[0] = li[r]
        li[r] = tmp

        # partion around the pivot, to find a rank of the chosen element
        #-------------
        j = 1
        
        for i in range(1,len(li)):
            if li[i] <= cur:
                # swap with the j
                tmp = li[j]
                li[j] = li[i]
                li[i] = tmp
                j += 1
            
        j -= 1
        tmp = li[0]
        li[0] = li[j]
        li[j] = tmp
        #--------------
        cur_rank = j + 1
        if k == cur_rank:
            return li[k-1]
        #if the random element have a rank not in range [n/3,2n/3], we redo everything
        if cur_rank > len(li) / 3 or cur_rank < 2*len(li)/3:
            break
    #print(cur,cur_rank,li)
    
    if k < cur_rank:
        return kselect(li[0:cur_rank-1],k)
    else:
        return kselect(li[cur_rank:],k-cur_rank)
    
class Node(object):
    def __init__(self):
        self._key = None
        self._line = None
        self._l = None
        self._r = None
        self._P = None
        #(xmin,xmax,ymin,ymax)
        self._area = (-math.inf,math.inf,-math.inf,math.inf)
        
        
class KdTree(object):
    def __init__(self):
        self._root = Node()
        universe_node = Node()
        
        self._root._p = universe_node
        self._range_query = []
        self._leaf = 0

    def build(self,li):
        self._root = self.build_recur(li,0)
    def build_recur(self,li,depth):
        
        if len(li) == 1:
            node = Node()
            node._key = li[0]
            return node
        li_tmp = []
        
        for i in li:
            li_tmp.append(i[depth % 2])               
        middle = kselect(li_tmp,len(li)//2+1)
    
        
        left_li = []
        right_li = []
 
        for i in li:
            
            if i[depth % 2] >= middle:
                right_li.append(i)
            if i[depth % 2] < middle:
                left_li.append(i)
        middle_node = Node()
        middle_node._line = middle
        
        if left_li != []:
            middle_node._l = self.build_recur(left_li,depth + 1)
        if right_li != []:
            middle_node._r = self.build_recur(right_li,depth + 1)
        if depth % 2 == 0:
            xmin,xmax,ymin,ymax = middle_node._area
            if left_li != []:
                middle_node._l._area = (xmin,middle,ymin,ymax)
            if right_li != []:
                middle_node._r._area = (middle,xmax,ymin,ymax)
        else:
            xmin,xmax,ymin,ymax = middle_node._area
            if left_li != []:
                middle_node._l._area = (xmin,xmax,ymin,middle)
            if right_li != []:
                middle_node._r._area = (xmin,xmax,middle,ymax)
        return middle_node

    def intersect(self,a1,a2):
        x1min,x1max,y1min,y1max = a1
        x2min,x2max,y2min,y2max = a2
        if (x1max < x2min or x2max < x1min or y1max < y2min or y2max < y1min):
            return False
        return True
    
    def query(self,area):
        self._range_query = []
        self.query_recur(self._root,area)
        return self._range_query
    def query_recur(self,node,area):
        if node == None:
            return
        if node._line == None: # if it's a leaf node a.k.a a point
            if node._key == None:
                return
            x,y = node._key
            xmin,xmax,ymin,ymax = area
            if (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
                self._range_query.append(node._key)
            return
        
        if self.intersect(area,node._l._area):
            self.query_recur(node._l,area)
        if self.intersect(area,node._r._area):
            self.query_recur(node._r,area)
        
##        self.query_recur(node._l,area)
##        self.query_recur(node._r,area)

    def count_leaf(self):
        self._leaf = 0
        self.count(self._root)
        return self._leaf
    def count(self,node):
        if node == None:
            return
        if node._key != None:
            self._leaf +=1
        
        self.count(node._l)
        self.count(node._r)
    
    
            
        
    
        

print('Reading input.....')          
num_set = set()
f = open('inputkd.txt','r')
for line in f:
    tmp = line.split(' ')
    num_set.add((int(tmp[0]),int(tmp[1])))
num_li = list(num_set)
print('Reading finish')
print('----------')

print('Doing range search by a linear scan.....')
area = (-10000,5000,-10000,10000)
start_time = time.time()
count = 0
for point in num_li:
    x,y = point
    xmin,xmax,ymin,ymax = area
    if (x >= xmin and x <= xmax and y >= ymin and y <= ymax):
        count += 1
print('Number of points in the area: ',count)
total_time = float(time.time()-start_time)
print("Linear scan search: %f seconds" % (total_time))
print('----------')


print('Building the Kd- Tree.....')
start_time = time.time()
k = KdTree()
k.build(num_li)
total_time = float(time.time()-start_time)
print("Bulding the Kd-Tree: %f seconds" % (total_time))
print('----------')

print('Doing range search by a linear scan.....')
start_time = time.time()
area = (-10000,5000,-10000,10000)
print('Number of points in the area: ',len(k.query(area)))
total_time = float(time.time()-start_time)
print("Kd tree range search: %f seconds" % (total_time))



    


            
 
 





