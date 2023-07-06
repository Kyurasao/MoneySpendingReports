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
            data_time = input('Enter the data and the time if the expense: ')
            payer = input('Enter the payer: ')
            details['payer'] = payer
            amount = input('Enter the amount: ')
            details['amount'] = amount
            category = input('Enter the category of the expense: ')
            details['category'] = category
            method = input('Enter the payment method: ')
            details['method'] = method
            value = input('To enter new expense - text "yes", to exit - text "no"')
            expense_dict[data_time] = details
    print(expense_dict)


if __name__ == '__main__':
    main()
