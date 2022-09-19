import os
import pandas as pd


#读取所有execl文件并拼接成一个dataframe
def read_excel(path):
    df = pd.DataFrame()
    for file in os.listdir(path):
        if file.endswith(".xlsx") and file.startswith("升级"):
            df = pd.concat([df, pd.read_excel(path + '\\' + file, dtype={'工单编号' : str})],axis=0,ignore_index=True)
    return df

#两个数组的交集
def intersection(a,b):
    return list(set(a) & set(b))


if __name__ == '__main__':
    path = r"D:\Code\移动数据\补充数据"
    df = read_excel(path)
    df.to_excel(path + '\\' + 'all_workorder.xlsx', index=False)