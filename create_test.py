import string
import random
##g = open("input.txt","w")
##co = 10000
##for i in range (co):
##    g.write(str(random.randint(0, co))+'\n')
##g.close()
##print('file created')


g = open("inputkd.txt","w")
co = 1000000
for i in range (co):
    sign = []
    num = []
    for j in range(2):
        tmp = random.random()
        if tmp < 0.5:
            num.append(random.randint(-co,0))
        else:
            num.append(random.randint(0,co))
    #print(num)
    
    g.write(str(num[0])+' '+ str(num[1])+'\n')
g.close()
print('file created')

