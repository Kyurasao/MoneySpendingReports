"""
This is a program for collecting expenses and issuing reports.
Users will be asked for information about their daily expenses and
a report on the amount of expenses for the day will be issued.
"""


def main():
    expense_list = []
    value = ' '
    while value:
        value = input('Израсходовынную сумму: ')
        if value == '':
            break
        else:
            expense_list.append(value)
    print(expense_list)


if __name__ == '__main__':
    main()
