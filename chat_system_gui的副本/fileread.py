"""
This file generates three test account into the user.csv. If these accounts get deleted,
run this file again and generate them again.
"""

import csv

headers = ['users', 'passwords']
user = {'users':'123', 'passwords':'123'}
userslist = [{'users':'1234', 'passwords':'1235'},{'users':'1', 'passwords':'1223'}]
with open('user.csv', 'w', encoding='utf8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    dict_writer = csv.DictWriter(f, fieldnames=headers)
    dict_writer.writerow(user)
    dict_writer.writerows(userslist)

target = '12346'
if __name__ == '__main__':

    with open('user.csv', 'r', encoding='utf8', newline='') as f:
        csv_DR = csv.DictReader(f)
        for row in csv_DR:
            print(row)
            if row['users'] != target:
                continue
            else:
                name = row['users']
                pwd = row['passwords']
                print(name, pwd)
                break
        else:
            print('false')













