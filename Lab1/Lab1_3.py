import math

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    list = {}
    #vasiot kod pisuvajte go tuka
    if m>n:
        print("nema podatoci")
        print("{}")
    else:
        for i in range(m,n+1):
            list[pow(i, 3)] = (i)
        if x>n:
            print("nema podatoci")
            print(list)
        else:
            for k, v in list.items():
                if x == k:
                    print(v)
            print(list)