def tambolenleribulma(sayi):
    tambolenler=[]

    for i in range(2,sayi):

        if(sayi % i ==0):
          tambolenler.append(i)
    return tambolenler

while True:

    sayi= input("Sayi:")

    if(sayi=="q"):
        print("Program Sonlandiriliyor...")
        break
    else:
        sayi= int(sayi)

        print("Tam Bolnler: ", tambolenleribulma(sayi))
