features = [[2, 0, 2, 2], [5, 3, 3, 5], [0, 3, 1, 2], [2, 8, 7, 6], [7, 1, 3, 2]]  # x
weights = (-1, 1, 1, -1, 1)  # w, weights[0] = w0 = -1
y = (1, 2, 3, 5, 8)
lf = len(features[0])  # feature's length

func = lambda i: weights[0] + sum(features[i][j] * weights[j + 1] for j in range(lf))
risk = lambda i: (y[i] - func(i)) ** 2
print(sum(risk(i) for i in range(len(y))))