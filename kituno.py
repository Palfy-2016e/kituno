jegyek = [5,5,5,5,5,3,5,5,5]
def atlag(jegyek):
    lista = []
    c=""
    for s in jegyek:
        if 5>=s:
            lista.append(s)
    a = sum(lista)
    if a%5==0:
        c="kituno"
    else:
        c="nem kituno"
    return c
print(atlag(jegyek))
