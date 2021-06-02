from matplotlib import pyplot as plt 
import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def sigmoid_p(x):
    return sigmoid(x) * (1 - sigmoid(x))
data = [[3, 1.5, 1],
[2, 1, 0],
[4, 1.5, 1],
[3, 1, 0],
[3.5, 0.5, 1],
[2, 0.5, 0],
[5.5, 1, 1],
[1, 1, 0]]
find_color_flower = [4.5, 1] 
# red flower 
plt.axis([0, 6, 0, 6])
plt.grid()
for i in range(len(data)): 
    point = data[i]
    color = "r"
    if point[2] == 0:
        color = "b"
    plt.scatter(point[0], point[1], c = color) 
plt.show()

w1 = np.random.randn() 
w2 = np.random.randn() 
b = np.random.randn()
learning_rate = 0.1 
costs = []
for i in range(10000):
    random_index = np.random.randint(len(data))
    point = data[random_index]
    z = point[0] * w1 + point[1] * w2 + b
    prediction = sigmoid(z)
    target = point[2]
    cost = np.square(prediction - target)
    if i % 100 == 0:
        cost_sum = 0
        for j in range(len(data)):
            point = data[j]
            z = point[0] * w1 + point[1] * w2 + b
            p_prediction = sigmoid(z)
            target = point[2]
            cost_sum += np.square(p_prediction - target) 
        costs.append(cost_sum)
    dxCost_pred = 2 * (prediction - target) 
    dxPred_dz = sigmoid_p(z)
    dz_dw1 = point[0] 
    dz_dw2 = point[1] 
    dz_db = 1
    dxCost_dw1 = dxCost_pred * dxPred_dz * dz_dw1 
    dxCost_dw2 = dxCost_pred * dxPred_dz * dz_dw2 
    dxCost_db = dxCost_pred * dz_db
    w1 = w1 - learning_rate * dxCost_dw1 
    w2 = w2 - learning_rate * dxCost_dw2 
    b = b - learning_rate * dxCost_db
plt.plot(costs) 
plt.show()

z = find_color_flower[0] * w1 + find_color_flower[1] * w2 + b 
pred = sigmoid(z)
if pred > 0.5:
    print("RED")
else:
    print("BLUE")
