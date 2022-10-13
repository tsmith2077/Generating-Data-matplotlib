import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.coolwarm, s=10)

# Set chart title and label axes
ax.set_title("Cubed Numbers")
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set tick style
ax.tick_params(axis='both', labelsize=14)

# Set range for each axis
ax.axis([0, 5000, 0, 125000000000])

plt.savefig('cubes_plot.png', bbox_inches='tight')