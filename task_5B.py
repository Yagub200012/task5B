a=input('''Привет! Взаимодействие с пользователем такое:
Игрок Х(крестик) и Игрок 0(нолик)
по очереди должны вводить координату очередного
хода. Игрок, построивший первым линию (горизонтальную, 
вертикальную или диагональную) побеждает.
Для подтверждения готовности введите любой символ: ''')
if a:
   b=[[' ',0,1,2],[0,'-','-','-'],[1,'-','-','-'],[2,'-','-','-']]
   def print_pole(pole):
       for i in range(4):
           print(*pole[i])
   print_pole(b)
   def proverka(pole): #Тут проверяются варианты победы
       for i in range(1,4):
           if (pole[i][1]==pole[i][2] and pole[i][1]==pole[i][3] and pole[i][1] != '-'):
               return pole[i][1]
       for j in range(1, 4):
           if (pole[1][j] == pole[2][j] and pole[1][j] == pole[3][j] and pole[1][j] != '-'):
               return pole[1][j]
       if (pole[1][1]==pole[2][2] and pole[1][1]==pole[3][3] and pole[2][2] != '-'):
           return pole[2][2]
       if (pole[1][3] == pole[2][2] and pole[1][3] == pole[3][1] and pole[2][2] != '-'):
           return pole[2][2]

   while not proverka(b):
       w1= int(input('''---------------------------------------------
       ведите номер строки: '''))+1
       w2 = int (input('введите номер столбца: '))+1
       w3= input('Введите свой символ (латинскую букву X или цифру 0): ')
       if (b[w1][w2] == '-'):
           b[w1][w2] = w3
       else:
           print ('Ячейка уже занята, попробуйте еще.')
       print_pole(b)
   if proverka(b):
       print('Победил пользователь ', proverka(b))