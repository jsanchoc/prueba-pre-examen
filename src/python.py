while True:
    print()
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Opción 3")
    try:
        opcion = int(input("Escoge una opción"))
    except:
        opcion == -1
    
    if opcion == 1:
        print(1+1)
    elif opcion == 2:
        print(2+2)
    elif opcion == 3:
        print(3+3)
