arr = [2, 4, 1, 6, 5, 40, -1]


def multiples(array):
    arset = set(array)
    complements = set()

    for number in array:
        complement = 20//number
        if number in complements:
            continue
        if complement in arset:
            print(number, complement)
        complements.add(complement)

multiples(arr)