def checksum(array, target_sum):
    seen = set()

    for num in array:
        complemento = target_sum - num

        if complemento in seen:
            return True

        # se agregara el numero al conjunto
        seen.add(num)
    return False

#Ejemplo
arr = [1, 3, 6, 9, 13]
target = 10

resultado = checksum(arr, target)
print(resultado)