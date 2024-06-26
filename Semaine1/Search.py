#collection de numbers
numbers = []
nb = int(input("combien de nombres : "))
for i in range(nb):
    num = int(input(f"nombre {i+1}: "))
    numbers.append(num)

#affichache des numbers
print(numbers)

# lire la valeur a rechercher.
search_nb = int(input("quel nombre a chercher? "))

# recherche sequentielle
position = -1
for i in range(len(numbers)):
    if search_nb == numbers[i]:
        position = i
        break
if position > -1:
    print(f"{search_nb} est a la position {position}")
else:
    print(f"{search_nb} n'existe pas dans le tableau")

# recherche dichotomique lorsque le tableau est trie
found = False
begin = 0
end = len(numbers) - 1
while not found and begin <= end:
    mid = (begin + end) // 2
    if search_nb == numbers[mid]:
        found = True
        print(f"nombre trouve a la position : {mid}")
    else:
        if search_nb < numbers[mid]:
            end = mid - 1
        else:
            begin = mid + 1

if not found:
    print("nombre inexistant")

#question 1: completer le code necessaire pour afficher la position de la valeur maximale dans numbers
max_position = numbers.index(max(numbers))
print(f"la valeur maximale est a la position {max_position}")

#question 2: completer le code necessaire pour afficher la position de la valeur minimale dans numbers
min_position = numbers.index(min(numbers))
print(f"la valeur minimale est a la position {min_position}")

#question 3: ecrire le code necessaire pour verifier si le tableau numbers est trie en ordre croissant
is_sorted_ascending = all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
if is_sorted_ascending:
    print("le tableau est trie en ordre croissant.")
else:
    print("le tableau n'est pas trie en ordre croissant.")

#question 4: considerons que le tableau est trie en ordre decroissant. implementer une methode de recherche dichotomique dans ce cas.
found = False
begin = 0
end = len(numbers) - 1
while not found and begin <= end:
    mid = (begin + end) // 2
    if search_nb == numbers[mid]:
        found = True
        print(f"nombre trouve a la position : {mid}")
    else:
        if search_nb > numbers[mid]:
            end = mid - 1
        else:
            begin = mid + 1

if not found:
    print("nombre inexistant dans le tableau trie en ordre decroissant.")
