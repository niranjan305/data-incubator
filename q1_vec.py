import numpy as np

def walk(x,y,m,n):
    if(np.random.rand()>0.5):
        if(x==m):
            y+=1
        else:
            x+=1
    else:
        if(y==n):
            x+=1
        else:
            y+=1
    return x,y


def random_walk(m,n,x,y):
    D = 0
    D_list= list()
    while True:
        x,y = walk_v(x,y,m,n)
        if(x==m) and (y==n):
            break
        D = max(((x/m)-(y/n)),((y/n)-(x/m)))
        D_list.append(D)
    return np.mean(D_list)    

length = 100000
m = 11
n = 7
x = np.zeros(length)
y = np.zeros(length)

walk_v = np.vectorize(walk,excluded=['m','n'])
random_walk_v = np.vectorize(random_walk,excluded=['m','n'])

D_mean = random_walk_v(m,n,x,y)
print("Mean: %12.10f" % np.mean(D_mean))
print("SD  : %12.10f" % np.std(D_mean))