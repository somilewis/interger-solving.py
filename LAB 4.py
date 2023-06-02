# Lewis Muthomi
# 1250 01
# 09/19/2022
# lab 4

# This program will allow you to enter two integer values then show you all 
# possible answers.

# user greating
print('Welcome to simple calculator')
print('Please enter only whole numbers')
print()

# Get user input
firstNumber = int(input('Please enter the first number: '))
secondNumber = int(input('Please enter the second number: '))
 
# Do math
addAnswer = firstNumber + secondNumber
divAnswer = firstNumber / secondNumber
truncAnswer = firstNumber // secondNumber
expoAnswer = firstNumber ** secondNumber
multAnswer = firstNumber * secondNumber
subAnswer = firstNumber - secondNumber
modAnswer = firstNumber % secondNumber

# display results
print(firstNumber, '+', secondNumber, '=', format(addAnswer,','))
print(firstNumber, '/', secondNumber, '=', format(divAnswer,',.2f'))
print(firstNumber, '//', secondNumber, '=', format(truncAnswer,','))
print(firstNumber, '**', secondNumber, '=', format(expoAnswer,','))
print(firstNumber, '*', secondNumber, '=', format(multAnswer,','))
print(firstNumber, '-', secondNumber, '=', format(subAnswer,','))
print(firstNumber, '%', secondNumber, '=', format(modAnswer,','))
print()

#exit message
print('Have a nice day!')
