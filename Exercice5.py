n = int(input("Combien de nombres voulez-vous insérer ? "))
numbers = []

for i in range(n):
    num = int(input("Insérez le nombre: "))
    numbers.append(num)

print("Les nombres divisibles par 5 sont :")
for num in numbers:
    if num % 5 == 0:
        print(num)
    