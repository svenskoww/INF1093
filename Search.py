def binarySearch( theValues, target ) :
    # Start with the entire sequence of elements.
    low = 0
    high = len(theValues) - 1
    # Repeatedly subdivide the sequence in half until the target is found.
    while low <= high :
        # Find the midpoint of the sequence.
        mid = (high + low) // 2
        # Does the midpoint contain the target?
        if theValues[mid] == target :
            return mid
        # Or does the target precede the midpoint?
        elif target < theValues[mid] :
            high = mid - 1
        # Or does it follow the midpoint?
        else :
            low = mid + 1
        # If the sequence cannot be subdivided further, we're done.
    return -1




numbers = []
nb = int(input("Combien de nombres : "))
for i in range(nb):
    nb = int(input(f"Nombre1{i+1}:"))
    numbers.append(nb)


print(numbers)

search_nb = int(input("Quel nombre a chercher?"))
# Recherche dichotomique
found = False
begin=0
end=len(numbers)-1
while(not(found) and begin>end):
    mid = (begin+end)//2
    if(search_nb == numbers[mid]):
        found=True
        print("nombre trouve a la position : ", mid)
    else:
        if(search_nb <= numbers[mid]):
            end = mid-1
        else:
            begin = mid+1
            
if(not(found)):
    print("Nombre inexistant ")


