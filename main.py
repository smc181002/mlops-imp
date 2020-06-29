from random import randint

accuracy = randint(50,80)
with open('command.txt', 'w') as file:
    file.write(str(accuracy))
print(accuracy)
