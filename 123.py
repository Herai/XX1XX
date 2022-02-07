#Print ("Hello World")

#print ("Hello World")

'''
Print Hello World

'''
#UserAge, UserName = 30, "Peter"

'''
x = 5
y = 10
y = x

print ("x = ", x)
print ("y = ", y)

'''

'''
Suponha x = 5, y = 2

- Adição 
x + y = 7

- Subtração
x - y = 3

- Multiplicação
x * y = 10

- Divisão
x / y = 2.5

- Divisão de Piso(Floor Division)
x // y = 2 (Arredonda a Resposta para o numero inteiro mais proximo)

- Modulo
x % y = 1 (Da o restante da divisão, quando 5 é dividido por 2, o resto é 1)

- Exponencial
x**2 = 25(5 elevado a 2)

-----------------------------------------------------------------------------------------------------------------------------------------

x += 2 significa a mesma coisa que  x = x + 2 
x -= 2 significa a mesma coisa que x = x - 2

Essa mesma questão vale para todos os outros simbolos

x *= 2 significa a mesma coisa que x = x * 2
x /= 2 significa a mesma coisa que x = x / 2
x //= 2 significa a mesma coisa que x = x // 2
x %= 2 significa a mesma coisa que x = x % 2 
x **= 2 significa a mesma coisa que x = x ** 2

-----------------------------------------------------------------------------------------------------------------------------------------

Inteiro = Numero sem virgula 

UserAge = 20, MobileNumber = 123456789

Float = Numero com virgula

UserHeight = 1.82,  UserWeight = 67.2

Sting = Texto

UserName = 'Peter', UserSpouseName = "Janet", UserAge = '30'

'Peter'.upper() = "PETER"

'''

#brand = 'Apple'
#ExchangeRate = 1.123456

#Message = 'The price of this %s laptop is %d USD and the exchage rate is %4.2f USD to 1 EUR ' % (brand, 1299, ExchangeRate)

#print(Message)

'''
Message = 'The price of this {0:s} laptop is {1:d} USD and the exchange rate is {2:4.2f} USD to 1 EUR'.format('Apple', 1299, 1.235)

print(Message)

'''

message1 = '{0} is easier than {1}'.format('Python', 'Java')

message2 = '{1} is easier than {0}'.format('Python', 'Java')

message3 = '{:10.2f} and {:d}'. format(1.234234234,12)

message4 = '{}'.format(1.234234234234)

print(message4)