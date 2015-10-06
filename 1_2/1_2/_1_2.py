while True :
    celcius = float(raw_input("What is the temprature in Celcius? "))
    if celcius < -273.14 :
       print("Error: Cannot go below absolute zero")
       
    else:
       fahrenheit = float((celcius + 32.00) * 1.80 )
       print("%.2f" % fahrenheit)
       break