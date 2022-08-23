with open('data.txt', 'r') as file:
    data = file.read()
    print ("data:", data)

    min_ascii = 1000000
    max_ascii = -1

    for char in data:
        print ("letter " + char + " has Ascii = " + str(ord(char)))

        if ord(char) == 10:
            continue

        if ord(char) < min_ascii:
            min_ascii = ord(char)
        if ord(char) > max_ascii:    
            max_ascii = ord(char) 

    print (chr(min_ascii), "is the smallest ascii having number = ", min_ascii) 
    print (chr(max_ascii), "is the largest ascii having number = ", max_ascii)
