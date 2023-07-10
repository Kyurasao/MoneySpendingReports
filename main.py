"""
This is a program for collecting expenses and issuing reports.
Users will be asked for information about their daily expenses and
a report on the amount of expenses for the day will be issued.
"""


def main():
    expense_dict = {}
    details = {}
    value = 'yes'
    while value == 'yes':
        if value == 'no':
            break
        else:
            data_time = input('Enter the data and the time if the expense, \ndd.mm.yyyy hh:mm:ss: \n')
            payer = input('Enter the payer: \n')
            details['payer'] = payer
            amount = input('Enter the amount: \n')
            details['amount'] = amount
            category = input('Enter the category of the expense, '
                             '\nhealth, clothes, eating out, food, trips, entertainments, connection, car, '
                             'payments, other : \n')
            details['category'] = category
            method = input('Enter the payment method, \ncard or cash: \n')
            details['method'] = method
            value = input('To enter new expense - text "yes", to exit - text "no": \n')
            expense_dict[data_time] = details
            with open('db.json', 'a+') as f:
                f.write(str(expense_dict) + '\n')


if __name__ == '__main__':
    main()
