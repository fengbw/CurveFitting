import numpy as np
import csv
import curveFitting
import matplotlib.pyplot as plt
import math

def doCompany():
    num = 0
    absMeanErr = 0.0
    relErr = 0.0
    sumErr = 0.0
    sumPrice = 0.0
    flag = True

    companyList = ['BILI','TWTR', 'BABA', 'AAPL', 'AMZN', 'AMD', 'FB' , 'GOOG', 'TSLA', 'V']
    while flag == True:
        company = input('Please input a company:')
        if company in companyList:
            f = open('src/' + company + '.csv', 'r')
            csv_f = csv.reader(f)
            data = []
            line_num = 0
            for row in csv_f:
                if line_num == 0:
                    line_num += 1
                    continue
                rows = float(row[1])
                data.append(rows)
            f.close()
            n = input('Please input the number of data (0 ~ ' + str((len(data) - 2)) + '): ')
            '''
            prediction = []
            actual = []
            index = []
            '''
            n = int(n)
            x = []
            for i in range(n):
                x.append(i+1)
            m = 9
            cf = curveFitting.curveFitting(x, data, m)
            prediction = cf.getMx(n + 1)
            s2x = cf.getS2(n + 1)
            actualPrice = data[n]
            num += 1
            sumErr += abs(actualPrice - prediction)
            sumPrice += actualPrice
            absMeanErr = sumErr / num
            relErr = sumErr / sumPrice
            print('Here is the predict result : ')
            print('--------------------------------------')
            print('Stock : ', company)
            print('predicted stock price : ', prediction)
            print('variance of prediction : ', s2x)
            print('actual price : ', actualPrice)
            print('absolute mean error : ', absMeanErr)
            print('average relative error : ', relErr)
            print('--------------------------------------')
            print('For n > 9, the line of actual and prediction...')
            predictions = []
            actuals = []
            index = []
            for n in range(9, len(data) - 2):
                x = []
                for i in range(n):
                    x.append(i + 1)
                m = 9
                cf = curveFitting.curveFitting(x, data, m)
                prediction = cf.getMx(n + 1)
                actualPrice = data[n]
                predictions.append(prediction)
                actuals.append(actualPrice)
                index.append(n)
            plt.plot(index, actuals, label = 'actual')
            plt.plot(index, predictions, label = 'prediction')
            plt.title('actual VS prediction')
            plt.show()
            plt.clf()

            conti = input('Continue?(Y/N):')
            if conti == 'Y':
                continue
            else:
                flag = False
            '''
            plt.plot(index,actual,label='actual')
            plt.plot(index, prediction,label='pre')
            plt.show()
            '''
        else:
            print('No this company!')

def doDemo():
    flag = True
    dataNameList = ['data1','data2', 'data3', 'data4', 'data5']
    while flag == True:
        dataName = input('Please input a data set:')
        if dataName in dataNameList:
            f = open('src/' + dataName + '.csv', 'r')
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
            n = 10
            x = []
            for i in range(n):
                x.append(i+1)
            m = 3
            cf = curveFitting.curveFitting(x, data, m)
            prediction = cf.getMx(n + 1)
            print('prediction for ' + dataName + ' is :', prediction)

            conti = input('Continue?(Y/N):')
            if conti == 'Y':
                continue
            else:
                flag = False

if __name__ == '__main__':
    choose = input('Do company prediction or demo data?(c/d)')
    if choose == 'c':
        doCompany()
    if choose == 'd':
        doDemo()
