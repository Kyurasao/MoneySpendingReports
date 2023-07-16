import requests

LINK = 'http://127.0.0.1:8000/expense/'


def get_expense(item_id: int):
    r = requests.get(LINK + str(item_id))
    return r.text


if __name__ == '__main__':
    for i in range(1, 10):
        result = get_expense(i)
        print(result)
