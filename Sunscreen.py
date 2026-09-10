while shining := input("Is the sun shining? yes/no: "):
    if shining == 'yes':
        while time := int(input('Enter a time between 0-23: ')):
            if 10 <= time <= 16:
                print("Use sunscreen")
            else:
                continue
    elif shining == 'no':
        break
    else:
        continue


           