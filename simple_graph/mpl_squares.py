import matplotlib.pyplot as plt

n = 10
input_values = [k for k in range(1, n + 1)]
squares = [k ** 2 for k in input_values]
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

ax.tick_params(axis='both', labelsize=14)

plt.show()
