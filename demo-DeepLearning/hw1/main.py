import sys
import pandas as pd
import numpy as np
# -*- coding:utf-8 -*-

# ��������
data = pd.read_csv('./train.csv',encoding = 'big5')

# preprocessiong ǰ����
# ȡ��Ҫ����ֵ���֣��� 'RAINFALL' ��λȫ���� 0
data = data.iloc[:, 3:]
data[data == 'NR'] = 0
raw_data = data.to_numpy()  #pandas.DataFrame.to_numpy()
                            # convert the DataFrame to a NumPy array


# ��ȡ����
# ��ԭʼ 4320 * 18 ����������ÿ���·������ 12 ��
# 18 (features) * 480 (hours) ������
month_data() = {}
for month in range(12):
    sample = np.empty([18, 480])
    for day in range(20):
            sample[:,day * 24 : (day + 1) * 24] = raw_data[18 * (20 * month]




# ÿ���»��� 480hrs��ÿ 9 Сʱ�γ�һ�� data
# ÿ���»��� 471 �� data������������Ϊ 471 * 12 ��
# ��ÿ�� data �� 9 * 18 �� features (һСʱ 18 �� features * 9 Сʱ)��
# ��Ӧ�� target ���� 471 * 12 ��(�� 10 ��Сʱ�� PM2.5)



# normalize ��һ��





# ��ѵ��������Ϊ��train_set"�͡�validastion_set"


# Training
# Adagrad�Ż���



# test
test_data = pd.read_csv('./test.csv', header = None, encoding = 'big5')



# prediction Ԥ��



# ��Ԥ�������浽CSV file��
