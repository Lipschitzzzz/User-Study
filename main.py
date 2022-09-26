import random

# shuffle
order_list = [1, 2, 3]
for i in range(0, 10):
    random.shuffle(order_list)
    # print(order_list)

import pandas

file1 = 'original csv/Condition 1.csv'
file2 = 'original csv/Condition 2.csv'
file3 = 'original csv/Condition 3.csv'
dataset1 = pandas.read_csv(file1)
dataset2 = pandas.read_csv(file2)
dataset3 = pandas.read_csv(file3)
participant_numbers = 8
question_numbers = 7

import re
# re = [R, month, Once a week, Multiple, E]

# print('dataset1')
# dataset1
column_name = []
participants = []
temp = []
for i in dataset1:
    column_name.append(i)
print(column_name)
for i in range(2, 9):
    # print(column_name[i], ': %.4f' % (dataset1[column_name[i]].sum() / participant_numbers))
    temp.append(dataset1[column_name[i]].sum() / participant_numbers)
x = sum(temp) / question_numbers
print("Condition1 final score: %.4f" % x)



temp.clear()
# print('dataset2')
# dataset2
column_name = []
for i in dataset2:
    column_name.append(i)
# print(column_name)
for i in range(2, 9):
    # print(column_name[i], ': %.4f' % (dataset2[column_name[i]].sum() / participant_numbers))
    temp.append(dataset2[column_name[i]].sum() / participant_numbers)
x = sum(temp) / question_numbers
print("Condition2 final score: %.4f" % x)





temp.clear()
# print('dataset3')
# dataset3
column_name = []
for i in dataset3:
    column_name.append(i)
# print(column_name)
for i in range(2, 7):
    # print(column_name[i], ': %.4f' % (dataset3[column_name[i]].sum() / participant_numbers))
    temp.append(dataset3[column_name[i]].sum() / participant_numbers)
x = sum(temp) / (question_numbers - 2)
print("Condition3 final score: %.4f" % x)


print(dataset1.iloc[:, 2:9].sum(axis = 1) / question_numbers, dataset1.iloc[:, 1])
print(dataset2.iloc[:, 2:9].sum(axis = 1) / question_numbers, dataset2.iloc[:, 1])
print(dataset3.iloc[:, 2:9].sum(axis = 1) / (question_numbers - 2), dataset3.iloc[:, 1])