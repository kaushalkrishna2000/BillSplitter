from random import randint

d = {};
a = []


def creator():
    n = int(input("Enter the number of friends joining (including you):"))

    if (n <= 0):
        print("\nNo one is joining for the party")
        return 0
    else:
        print("\nEnter the name of every friend (including you), each on a new line:")
        for i in range(n):
            name = input()
            d[name] = 0;
            a.append(name)
        print()
        return 1

def splitter(totbill, n):
    com = round(totbill / n, 2)
    for i in d:
        d[i] = com

def lucky():
    ch = input('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:').lower()
    if ch == 'yes':
        l = randint(0, len(d) - 1)
        print(f'\n{a[l]} is the lucky one!')
        return a[l]
    else:
        print('\nNo one is going to be lucky')
        return "nota"

def mainf():
    if creator():
        totbill = int(input("Enter the total bill value:"))

        name = lucky()

        if name != "nota":
            splitter(totbill, len(d) - 1)
            d[name] = 0
        else:
            splitter(totbill, len(d))

        print()
        print(d)


mainf()
