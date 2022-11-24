__operators = ('+', '-', '/', '//', '*', '**', '%')


def calculator():
    x = eval(input())
    operator = input()
    y = eval(input())

    #print(str(x) + operator + str(y))

    # your code here

    if operator == '+':
        rezultat = x+y
        print(rezultat)
    elif operator == '-':
        rezultat = x-y
        print(rezultat)
    elif operator == '/':
        rezultat = x/y
        print(rezultat)
    elif operator == '//':
        rezultat = x//y
        print(rezultat)
    elif operator == '*':
        rezultat = x*y
        print(rezultat)
    elif operator == '**':
        rezultat = x**y
        print(rezultat)
    elif operator == '%':
        rezultat = x%y
        print(rezultat)
    else: print("Netocno vneseni podatoci")




if __name__ == "__main__":
    calculator()
