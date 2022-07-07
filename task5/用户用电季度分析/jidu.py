import pandas as pd

inputfile = "D:/Desktop/任务5/用户用电季度分析/inputfile/Tianchi_.xlsx"
outfile = "D:/Desktop/任务5/用户用电季度分析/outfile/Tianchi_out.csv"
data = pd.read_excel(inputfile)

for i in range(1, 1454):
    value = data[((data['Month'] == 12) | (data['Month'] == 1) | (data['Month'] == 2)) & (
            data['user_id'] == i)].power_consumption.sum()
    avg = value / 90
    data.loc[(data['user_id'] == i), 'one'] = avg  # one-冬
    # print(data)
    # for i in range(1,1454):

    value1 = data[((data['Month'] == 3) | (data['Month'] == 4) | (data['Month'] == 5)) & (
            data['user_id'] == i)].power_consumption.sum()
    avg1 = value1 / 90
    data.loc[(data['user_id'] == i), 'two'] = avg1  # two-春
    # print(data)
    # for i in range(1,1454):

    value2 = data[((data['Month'] == 6) | (data['Month'] == 7) | (data['Month'] == 8)) & (
            data['user_id'] == i)].power_consumption.sum()
    avg2 = value2 / 90
    data.loc[(data['user_id'] == i), 'three'] = avg2    # three-夏
    # print(data)
    # for i in range(1,1454):

    value3 = data[((data['Month'] == 9) | (data['Month'] == 10) | (data['Month'] == 11)) & (
            data['user_id'] == i)].power_consumption.sum()
    avg3 = value3 / 90
    data.loc[(data['user_id'] == i), 'four'] = avg3     # four-秋
    # print(data)
data.to_csv(outfile)
