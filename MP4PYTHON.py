import math 
from matplotlib import pyplot as plt
def Projectile_Trajectory(D,V,angle,ax,ay):
    
    
    if ay==0:
        print("ERROR: 0 cannot be considered as value for vertical acceleration")
        return  
    
    x_vals = [] 
    y_vals = [] 
   
    v0x = V*math.cos(angle*(3.141/180)) 
    v0y = V*math.sin(angle*(3.141/180)) 
    
    t = 0
    x = 0
    y = D 
    delta = 0.0001 
    
    x_vals.append(x)
    y_vals.append(y)
    
    while(True):
        t = t+delta
        x = v0x*t + (0.5)*ax*(t*t)
        y = v0y*t + (0.5)*ay*(t*t) + D
        
        x_vals.append(x)
        y_vals.append(y)
        
        if y < delta:
            break
        
    plt.plot(x_vals,y_vals)  
    ax = plt.gca()
    ax.set_ylim([0,max(y_vals)])
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    plt.title('Projectile Trajectory')
    plt.grid()
    plt.show()
        
if __name__ == '__main__':
   D = 12 
   V = 18 
   angle = 53 
   ax = 0 
   ay = -9.81
   Projectile_Trajectory(D,V,angle,ax,ay)  