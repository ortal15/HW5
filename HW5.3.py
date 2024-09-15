#START
x: float=float(input('enter your height:'))
while 0.4<=x<=2.5:
    print('okay')
    break
else:
    print('wrong input')
    x: float = float(input('enter your height:'))

#END

#START
x: int=int(input('enter a number:'))
y: int=int(input('enter a number:'))
if y>x:
    for z in range (x,y+1):
        print(z,end='')
else:
    for z in range (x,y-1,-1):
        print(z,end='')
#END

#START
count = 1
pie: float = float(input('pie is:'))
while pie != 3.14:
    count += 1
    print('try again')
    pie: float = float(input('pie is:'))
    if count > 3:
        print('wrong pie is 3.14')
        break
else:
    print('correct')

# END

#START
while 1:
    number1: int = int(input('enter a 1number:'))
    number2: int = int(input('enter a 2number:'))
    number3: int = int(input('enter a 3number:'))
    if (0 < number1 <= 10) and (10 < number2 < 60) and (60 < number3 < 100) and ((number1 + number2 + number3) / 3 == number2):
        break
    else:
        print('wrong input')
# END

# START
beer = 10
age: int = int(input('enter your age:'))
count = 1
while beer:
    if 18 <= age:
        count += 1
        print('you get a beer!!😊😊')
        beer -= 1
        print(f'{beer} beers left')
    if count < 10:
        age: int = int(input('enter your age:'))
    else:
        print('no beers left')
# END
