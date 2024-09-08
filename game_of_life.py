# game_of_life.py grace and sarayu
"""
CS1112 Project 4 Game of Life

Refer to the Project 4 description for details and other helpful information.

To to see the animation, in the Spyder Python Console, type
    %matplotlib qt
to send the graphics to the qt graphical user interface.  You only need to do
this once in a session (unless you restart the kernel).

"""
import numpy as np
import matplotlib.pyplot as plt
import random
import copy 


def create_world(nr, nc, data_mode):
    """
    Returns an nr-by-nc array of ints representing the game of life world
    
    Parameters
    ----------
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two kinds:
        
    - The string "random".  Then the initial state is to be randomly generated.
      The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
    - The string name of a plain text file storing the initial state.  If the
      world read from the file is bigger than nr-by-nc, use only the rows and
      columns of data that fit on the nr-by-nc array to be returned
    """
    pass  # TO-DO: implement this function 
    world=np.zeros((nr,nc))
    if data_mode=="random":
        for i in range(nr):
            for j in range(nc):
                r = random.random()
                if r<(1/(abs(i-j)+2)):
                    world[i,j]=1
    if data_mode == 'seeds_p48.txt':
         #text file from data
        data = np.loadtxt('seeds_p48.txt', 'int',  '#')
        nr_d, nc_d = data.shape
        for i in range(min(nr, nr_d)):
            for j in range(min(nc, nc_d)):
                world[i, j] = data[i, j]
    if data_mode == 'seeds_glider.txt':
        data = np.loadtxt('seeds_glider.txt', 'int',  '#')
        nr_d, nc_d = data.shape
        for i in range(min(nr, nr_d)):
            for j in range(min(nc, nc_d)):
                world[i, j] = data[i, j]
     
        
  #  print(world)
                    
  #print((1/(abs(i-j)+2)))
                
#else pass through plain text file and read that and generate initial state (rpoblem for later)

    return world


def one_generation_later(w, add_rule):
    """
    Returns a new array representing the world matrix w after ONE generation
    according to the rules of the game of life

    Parameters
    ----------
    w : the world matrix, a 2-d array.
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule. ignore for now 
    
    """
    
    (nr,nc)=np.shape(w) #you want to be able to access w in terms of nr and nc
    w1 = copy.deepcopy(w) # make a copy of this world becuase you dont want to edit on the original matrix 
    for i in range(nr):
        for j in range (nc):
            C=nearest_neighbors(w,i,j,1) #call the helper function
            count=np.sum(C) #the helper function counts every alive point surrounding the point you are on including itself
            if count<3 and w[i,j]==1: 
            # since nearest_neighbors will double count if the point you are on is alive, adjust the conditionals by +1 for when the point you are on is currently live by
                w1[i,j] = 0
            if (count==3 or count ==4) and w[i,j]==1:
                w1[i,j]=1 
            if(count>4 and w[i,j]==1):
                w1[i,j]=0
            if(count==3 and w[i,j]==0):
                w1[i,j]=1
            if add_rule==True and count >3: # prob. life rule 
                prob = random.random()
                if(prob< 0.4):
                    w1[i,j]=1
    #print('one_generation_later')
    w = w1 #update your world with your edited world once done editing 
  #  print(w)            
    return w

def simulate(n, nr, nc, data_mode, add_rule, blink):
    """
    Returns the world matrix after simulating n generations of the game of life
    
    Parameters
    ----------
    n : the number of generations (steps), a non-negative int
    
    nr : the number of rows in the world.  An int > 5.
    
    nc : the number of columns in the world.  An int > 5.
    
    data_mode : (string) can be one of two things:
        
     - The string "random". Then the initial state is to be randomly generated.
     The element at [i,j] is 1 with probability 1/(abs(i-j)+2); otherwise 0.
        
     - The string name of a plain text file storing the initial state.  If the
        world read from the file is bigger than nr-by-nc, use only the rows and
        columns of data that fit on the nr-by-nc array to returned
    
    add_rule: (bool) If True, apply extra-life-rule; 
              otherwise do not apply extra-life-rule.
              
    blink : a positive float.  blink > 1 means no animation
            blink <= 1 is the blink rate of the animation, i.e., the pause time
            in seconds between generations 
    """
    

    if data_mode == "random":
        world= create_world(nr, nc, "random")
        plt.close()
        fig, ax = plt.subplots() 
        ax.matshow(world)
        ax.set_title(f'Generation {0}')
        plt.pause(blink) 
    
        for i in range(n):
            world= one_generation_later(world, add_rule)
            ax.clear()
            ax.matshow(world)
            ax.set_title(f'Generation { i+1}')
            plt.pause(blink)
            plt.show()
    
    else:
        world= create_world(nr, nc, data_mode)
        plt.close()
        fig, ax = plt.subplots() 
        ax.matshow(world)
        ax.set_title(f'Generation {0}')
        plt.pause(blink) 
    
        for i in range(n):
            world= one_generation_later(world, add_rule)
            ax.clear()
            ax.matshow(world)
            ax.set_title(f'Generation { i+1}')
            plt.pause(blink)
            plt.show()
        
        return world

            
#### TO-DO: Specify and implement at least one helper function here

def nearest_neighbors(arr,index_x,index_y,distance):
    # where arr is the matrix of all alive and dead
    #index_x is x index in arr 
    #index_y is y index in arr
    #distance is distance from alive point 
    
    (nr,nc)=np.shape(arr)
    imin=max(0,index_x-distance)
    imax=min(nr,index_x+distance+1)
    jmin=max(0,index_y-distance)
    jmax=min(nc,index_y+distance+1) 
    C=arr[imin:imax,jmin:jmax]
    return C


#### Script code

if __name__ == "__main__":
    
    # This is a convenient place to write code to test your functions 
    # individually as you develop your program!!

    # TO-DO: Add more code here and execute the script for testing
    
        nr= 20
        nc= 20
        n=20
      #  data_mode = "random"
       # data_mode = 'seeds_glider.txt'
        data_mode = 'seeds_p48.txt'
        add_rule = False
        blink = 0.5 
        world= simulate(n, nr, nc, data_mode, add_rule, blink)
   # print(world)
    