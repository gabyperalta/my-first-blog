print('Hello, Django girls!')

if 3 > 2:
    print('A trabajar')

if 5 > 2:
    print('5 es mayor que 2')
else:
    print('5 no es mayor que 2')

nombre = 'Sonja'
if nombre == 'Ola':
    print('Hey Ola!')
elif nombre == 'Sonja':
    print('Hey Sonja!')
else:
    print('Hey anonymous!')

def hola():
    print('Hi there!')
    print('How are you?')

hola()

def hola2(nombre):
    if nombre == 'gaby':
        print('Hi gaby!')
    elif nombre == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')

hola2('brenda')

def hola3(nombre):
    print('Hola ' + nombre+ '!')

hola3("Rachel")

#bucles
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hola3(name)
    print('Next girl')

for i in range(1, 6):
    print(i)
