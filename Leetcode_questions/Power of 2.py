def powerTwo(ing):
    i=0
    for i in range(0,ing):
        if ing==2**i:
            return True


    return False

print(powerTwo(2))