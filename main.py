"""
This is a program for collecting expenses and issuing reports.
Users will be asked for information about their daily expenses and
a report on the amount of expenses for the day will be issued.
"""
import json
import time
from pathlib import Path
from typing import List

CATEGORIES = {
    '01': 'health',
    '02': 'clothes',
    '03': 'eating out',
    '04': 'food',
    '05': 'trips',
    '06': 'entertainments',
    '07': 'connection',
    '08': 'car',
    '09': 'payments',
    '99': 'other',
}


def create_expense(expenses: List):
    details = {}

    print(f"Let's enter expenses data...")
    date_time_string = input("Enter time of expense | 'now' orr date in format [dd.mm.yyyy hh:mm:ss]: ")
    date_time = time.strftime('%d.%m.%Y %H:%M:%S',
                              time.localtime(time.time())) if date_time_string == 'now' else date_time_string
    details['payer'] = input('Who payed: ')
    details['amount'] = input('How much: ')
    category_string = input('Enter the category of the expense (use numbers): \n'
                            '[01] health | [02] clothes | [03] eating out | [04] food | '
                            '[05] trips \n[06] entertainments | [07] connection | [08] car | '
                            '[09] payments | [99] other :')

    details['category'] = CATEGORIES.get(category_string, 'other')
    details['method'] = input('Enter the payment method, card or cash:')

    # adding details to list of expenses
    expenses.append({date_time: details})


def main():
    # read db file
    p = Path('db.json')
    with p.open('r') as file:
        file_data = file.read()
        expenses: List = json.loads(file_data) if file_data else []

    while True:
        value = input("type: 'exit' to exit | 'list' to list all expenses "
                      "| 'create' to create more | [number of the line] to edit ")
        if value == 'exit':
            break
        elif value == 'create':
            create_expense(expenses=expenses)
        elif value == 'list':
            for index, expense in enumerate(expenses):
                print(f'[{index + 1}] {expense}')
        elif value.isdigit():
            if 0 < int(value) <= len(expenses):
                print(expenses[int(value)-1])
            else:
                print(f'wrong value, we have only [1:{len(expenses)}]')
        else:
            print(f'Unknown value. Once again...')

            # saving final data
    with p.open('w+') as file:
        json.dump(expenses, file)


if __name__ == '__main__':
    main()
