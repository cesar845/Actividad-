print('Cuanto se debe regar en diversos cultivos')
papa = 0
yuca = 0
zanahoria = 0

cultivosStr = int(input('Seleccione el cultivo que va regar -> \n1. Papas\n2. Yucas\n3. Zanahorias\n-> '))
if cultivosStr == 1:
    for i in range(3):
        litrospapaInt = int(input('Cuantos litros regó -> '))
        papa += litrospapaInt
    print('Total de litros regados esta semana son',papa)    
elif cultivosStr == 2:
    for i in range(2):
        litrosyucaint = int(input('Cuantos litros regó -> '))
        yuca += litrosyucaint
    print('Total de litros regados esta semana son',yuca)
elif cultivosStr == 3:
    for i in range(2):
        litroszanahoriaInt = int(input('Cuantos litros regó -> '))
        zanahoria += litroszanahoriaInt
    print('Total de litros regados esta semana son',zanahoria)