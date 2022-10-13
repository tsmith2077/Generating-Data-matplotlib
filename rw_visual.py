import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
# Make a random walk.
    rw = RandomWalk(50000)
    rw.fill_walk()

    # Plot the the line of a pollen grain on a water drop
    plt.style.use('classic')
    fix, ax = plt.subplots(figsize=(15,9))
    point_numbers = range(rw.num_points)
    # ax.plot(rw.x_values, rw.y_values, linewidth=3)
    
    # Plot the points of a random walk
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=1)
    
    #Emphasize the first and last points.
    # ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    # ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    #            s=100)
    
    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n):  ")
    if keep_running == 'n':
        break