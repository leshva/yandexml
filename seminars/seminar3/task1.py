func = lambda x: 3 * x - 5
dataset = ((2,2),(2,1),(5,9),(-3,-10),(0,-5),(3,3))

print(sum((y - func(x)) ** 2 for x, y in dataset))