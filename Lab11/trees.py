import matplotlib.pyplot as plt

def harvestPlant(initial_trees, rate_harvested =.12, trees_planted=600):
    # Simulates one year at given conditions
    return initial_trees - int(initial_trees * rate_harvested) + trees_planted
    

years = eval(input("How many years forward should be calculated?\n"))
total_trees = int(input("How many initial trees are there?\n"))
rate = float(input("At what rate are trees harvested per year?\n"))
planted = int(input("How many new trees are planted each year?\n"))
plt.plot(0, total_trees, 'bo')
for y in range(years):
    total_trees = harvestPlant(total_trees, rate, planted)
    plt.plot(y+1, total_trees, 'bo')

print(total_trees)

plt.xlabel("Years")
plt.ylabel("Number of Trees")
plt.title("Number of Trees vs Years")
plt.grid(True)
plt.show()