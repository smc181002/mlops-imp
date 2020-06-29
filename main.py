from random import randint
import sys

try:
  hyperParams = int(sys.argv[1])
except:
  print('enter a number and not any other datatype.')


accuracy = randint(70, hyperParams)
with open('command.txt', 'w') as file:
    file.write(str(accuracy))
print(accuracy, hyperParams)
