while True:    
    fahrenheit = float(raw_input("What is the temprature in Fahrenheit? "))
    celcius = float((fahrenheit - 32.00) / 1.80 )
    if celcius < -273.15:
        print "can't go below absolute zero"
    else:
        print("%.2f" % celcius)