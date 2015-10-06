while True:
    value = float(raw_input("Give me a number: "))
    if value < 0 :
        result = int(value) / int(-1)
    else:
        result = value
    print("The absolute value of the number is", int(result))