a = int(raw_input('A? '))
b = int(raw_input('B? '))
c = int(raw_input('C? '))
if a > b:
    # a > b
    if a > c:
        # a > b e a > c
        maior = a
        if b > c:
            # a > b > c
            meio = b
            menor = c
        else:
            # a > c > b
            meio = c
            menor = b
    else:
        # c > a > b
        maior = c
        meio = a
        menor = b
else:
    # b > a
    if b > c:
        # b > a e b > c
        maior = b 
        if a > c:
            # b > a > c
            meio = a
            menor = c
        else:
            # b > c > a
            meio = c
            menor = a
    else:
        # c > b > a
        maior = c
        meio = b
        menor = a
print maior, meio, menor
