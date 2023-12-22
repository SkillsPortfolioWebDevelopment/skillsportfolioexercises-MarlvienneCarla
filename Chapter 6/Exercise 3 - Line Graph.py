import matplotlib.pyplot as plt

# Line from (1, 2) to (6, 8)
line1_x = [1, 6]
line1_y = [2, 8]

# Dotted line from (1, 3) to (2, 8) to (6, 1) to (8, 10)
line2_x = [1, 2, 6, 8]
line2_y = [3, 8, 1, 10]

# Plotting the lines
plt.plot(line1_x, line1_y, label='Line 1')
plt.plot(line2_x, line2_y, linestyle='dotted', label='Dotted Line')

# Set axis labels
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Add a legend
plt.legend()

# Display the plot
plt.show()
