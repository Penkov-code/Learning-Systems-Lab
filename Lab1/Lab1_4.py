def shift(seq, n):
    n = n % len(seq)
    return seq[n:] + seq[:n]


if __name__ == '__main__':
    l = list(map(int, input().split(' ')))
    k = int(input())

    lista = [x for x in l]
    print(shift(l,k))

    # vashiot kod pishuvajte go tuka
