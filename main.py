from random import randint

accuracy = randint(70,90)
with open('command.txt', 'w') as file:
    file.write(str(accuracy))
print(accuracy)
