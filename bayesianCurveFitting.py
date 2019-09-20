import numpy as np
import math
import csv
import matplotlib.pyplot as plt

def bayesian(data):
    x_10 = []
    t_data = []
    for i in range(len(data) - 10, len(data)):
        t_data.append(data[i])
    for i in range(1, 11):
        x_10.append(i)
    t = []
    t.append(t_data)
    t_data = t
    N = 10
    M = 6
    rel_err_dr = 0
    x = x_10[len(x_10) - 1] + 1
    for k in range(1):
        t = np.zeros((N, 1), float)
        phi = np.zeros((M, 1), float)
        phi_sum = np.zeros((M, 1), float)
        phi_sum_t = np.zeros((M, 1), float)
        for i in range(M):
            phi[i][0] = math.pow(x, i)
        for i in range(N):
            t[i][0] = t_data[k][i]
        for j in range(N):
            for i in range(M):
                phi_sum[i][0] += math.pow(x_10[j], i)
                phi_sum_t[i][0] = phi_sum_t[i][0] + t[j][0] * math.pow(x_10[j], i)

        S = np.linalg.inv(0.005 * np.identity(M) + 11.1 * np.dot(phi_sum, phi.T))
        var = np.dot((phi.T), np.dot(S,phi))
        var = var + 1 / 11.1

        mean = 11.1 * np.dot(phi.T, np.dot(S,phi_sum_t))
        mean = mean[0][0]
        print('Mean: ', mean)

    t = t_data[0]
    t_data = t
    sum = 0
    avg = 0
    print('t_data: ', t_data)
    for i in t_data:
        sum = sum + i
    mov = sum / len(t_data)
    print('Mov: ', mov)
    per = ((mean -mov) / mov) * 100
    print('Per: ', per)
    final = []
    mean = round(mean, 3)
    per = round(per, 3)
    final.append(mean)
    final.append(per)
    return(final)

def draw(data, prediction):
    num = []
    for i in range(len(data)):
        num.append(i)
    plt.plot(num, data, marker = 'o')
    plt.plot(num, prediction, marker = '*')
    plt.legend()
    plt.show()

f = open('src/AMZN.csv', 'r')
csv_f = csv.reader(f)
data = []
line_num = 0
for row in csv_f:
    if line_num == 0:
        line_num += 1
        continue
    rows = float(row[1])
    data.append(rows)
print(data)
f.close()

prediction = bayesian(data)
print(prediction)
