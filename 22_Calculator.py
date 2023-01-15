
#Calculator

#Add

def add(n1,n2):
    return n1+n2

#Subtract

def subtract(n1,n2):
    return n1-n2

#Multiply
def multiply(n1,n2):
    return n1*n2

#Divide
def divide(n1,n2):
    return n1/n2

operation = {
    
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide,
}

        
num1 = int(input("What´s is the first number?: "))
for simbol in operation:
    print(simbol)

symbol = input('Pick an operation from the line above: ')

num2 = int(input("What´s is the second number?: "))

calculation_function = operation[symbol]
answerd = calculation_function(num1,num2)

    
print(f'{num1} {symbol} {num2} = {answerd}')