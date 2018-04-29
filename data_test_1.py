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
    #print(loc)
f = open("data1.csv","w")
def random_walk(D_mean,m,n):
    for i in range(len(D_mean)):
        D_list = list()
        x=0
        y=0
        while True:
            x,y = walk(x,y,m,n)
            if (x==m) and (y==n):
                break
            D = max(((x/m)-(y/n)),((y/n)-(x/m)))
            D_list.append(D)
        D_mean[i] = np.mean(D_list)
        f.write("%12.10f\n" % D_mean[i])
    return D_mean

m = 11
n = 7
D_mean = np.zeros(100)
D_mean_1 = random_walk(D_mean,m,n)
f.close()
print("Mean    : %12.10f" % np.mean(D_mean_1))
print("Std. Dev: %12.10f" % np.std(D_mean_1))