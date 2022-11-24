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
            list[i] = (pow(i,2), pow(i,3), math.sqrt(i))
        if x>n:
            print("nema podatoci")
            print(list)
        else:
            print(list.get(x))
            print(list)