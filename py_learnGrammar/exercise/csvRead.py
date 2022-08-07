
def read_csv(csvfile,has_coloumn = True):
    with open('./userpass.csv') as f:
        line_list = f.readlines()

    if not has_coloumn:
        raise Exception('csv文件必须要使用第一行作为列名')
        # return None 
    key_list = line_list[0].strip().split(',')

    list = []
    for i in range(1,len(line_list)):
        if line_list[i].startswith('#'):
            continue
        temp_list = line_list[i].strip().split(',')

        dict = {}
        for j in range(len(key_list)):
            dict[key_list[j]] = temp_list[j]

        list.append(dict)
    return list     

# result = read_csv('./userpass.csv',has_coloumn=True)
# print(result)

# 使用csv模块读写
import csv

with open('./user-2.csv') as f:
    csv_list = csv.reader(f)
    for item in csv_list:
        print(list(csv_list))