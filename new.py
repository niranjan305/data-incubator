from __future__ import division
import numpy as np

# Function for calculating the running grand mean
def new_G_mu(G_mu,mu,j):
    G_mu = G_mu+(mu-G_mu)/j
    return G_mu
    
# Function for calculating the running mean
def new_mu(mu,D,i):
    mu = mu+(D-mu)/i
    return mu

# Function for advancing the ant one unit length north
def walk_north(m,n,x,y):
    # if the ant has reached northmost border advance in east direction
    if x==m and y<n:
        y+=1
    elif x<m:
        x+=1
    return x,y

# Function for advancing the ant one unit length east
def walk_east(m,n,x,y):
    # if the ant has reached the eastern most border advance north
    if y==n and x<m:
        x+=1
    elif y<n:
        y+=1
    return x,y

# Function to decide if ant moves north or east
def new_position(m,n,x,y):
    if(np.random.rand()>0.5):
        x,y = walk_north(m,n,x,y)
    else:
        x,y = walk_east(m,n,x,y)
    return x,y

# Function for calculating running mean SD
def new_sd(sd,mu,k,D,mu_n):
    sd_n = ((k-2)*sd + (D-mu_n)*(D-mu))/(k-1)
    return sd_n

# Function for calculating running grand SD
def new_G_sd(G_sd,sd,k,G_mu,sd_n):
    G_sd_n = ((k-2)*G_sd + (mu-sd_n)*(mu-sd))/(k-1)
    return G_sd_n

# Parameters for the code
ACC = 10 # Accuracy upto decimal places
# grid size
m = 11 
n = 7

# Initialize a lot of variables
x = 0 
y = 0
mu = 1
mu_n = 0
sd = 1
sd_n = 0
i=1
j=1
G_mu = 1
G_mu_n = 0
G_sd = 1
G_sd_n = 0
P_greater_than_2 = 0
P_greater_than_6 = 0
cnt = 1

# Run the loop till the grand mean at steps N and N-1 do not match upto decimal places 
# specified by the ACC parameter
while round(G_mu,ACC) != round(G_mu_n,ACC):
    if x < m or y<n:
        x,y = new_position(m,n,x,y)
    else:
	# Once the ant reaches outermost point, calculate grand mean and SD
	# Also this means one trajectory is over, so move ant again to starting
        # place i.e. x=0 and y=0
        x=0
        y=0
        G_mu = G_mu_n
        G_mu_n = new_G_mu(G_mu,mu_n,j)
        if(j>=3):
            G_sd = G_sd_n
            G_sd_n = new_G_sd(G_sd,sd,j,G_mu,sd_n)
        mu_n = 0
        sd_n = 0
        i=1
        j+=1
    D = max(((x/m)-(y/n)),((y/n)-(x/m)))
    if D>0.2:
	P_greater_than_2 += 1
	if D>0.6:
		P_greater_than_6 += 1
    # Till we are in the same trajectory keep track of running mean and SD
    mu = mu_n
    mu_n = new_mu(mu,D,i)
    if(i>=3):
        sd = sd_n
        sd_n = new_sd(sd,mu,i,D,mu_n)
    i+=1
    cnt+=1

print("Mean: %12.10f" % G_mu)
print("Std Dev: %12.10f" % G_sd_n)
print("Event A count (D>0.2): %d" % P_greater_than_2)
print("Event B count (D>0.6): %d" % P_greater_than_6)
print("Total events: %d" % cnt)
P = (P_greater_than_6/cnt)/(P_greater_than_2/cnt)
print("P(D>0.6)|P(D>0.2) when m=%d and n=%d: %12.10f" %(m,n,P))


