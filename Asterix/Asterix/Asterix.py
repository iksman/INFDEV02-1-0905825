try:    
    start = int(input("Give me an integer> "));
    end = 0 
    startup = start + 2
    print("0" * startup);
    while start != -1:
        print("0" + "*" * start + " " * end + "0")
        start = start - 1
        end = end + 1
    print("0" * startup);
except ValueError:
    print("That's no integer!");

