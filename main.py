"""
This is a program for collecting expenses and issuing reports.
Users will be asked for information about their daily expenses and
a report on the amount of expenses for the day will be issued.
"""


def main():

    # def add_func():
    #
    # expense_dict = {}
    # details = {}
    # value = 'yes'
    # while value == 'yes':
    #     if value == 'no':
    #         break
    #     else:
    #         data_time = input('Enter the data and the time if the expense, \ndd.mm.yyyy hh:mm:ss: \n')
    #         payer = input('Enter the payer: \n')
    #         details['payer'] = payer
    #         amount = input('Enter the amount: \n')
    #         details['amount'] = amount
    #         category = input('Enter the category of the expense, '
    #                          '\nhealth, clothes, eating out, food, trips, entertainments, connection, car, '
    #                          'payments, other : \n')
    #         details['category'] = category
    #         method = input('Enter the payment method, \ncard or cash: \n')
    #         details['method'] = method
    #         value = input('To enter new expense - text "yes", to exit - text "no": \n')
    #         expense_dict[data_time] = details
    #         with open('db.json', 'a+') as f:
    #             f.write(str(expense_dict) + '\n')

    # def edit_func():

    try:
        with open('db.json', 'r') as f:
            # print('Choose one string to edit it')
            i = 0
            for line in f:
                i += 1
                print(i, line.strip())
    except:
        print('A database file not exist yet, add a expense to creat a new one')

    num = int(input('Choose the number of string to edit it: \n'))
    with open('db.json', 'r') as f:
        for i, line in enumerate(f):
            if i == num - 1:
                print(line, end='')
                break
        if i != num - 1:
            print('Строки с таким номером нет')

    with open('db.json', 'r') as NewPrj_kv:
        lines = NewPrj_kv.readlines()

    # print(lines)
    new_line = input('enter new line: ')
    del lines[num]
    lines.insert(2, new_line + '\n')

    with open('db.json', 'w') as NewPrj_kv:
        NewPrj_kv.writelines(lines)


if __name__ == '__main__':
    main()
