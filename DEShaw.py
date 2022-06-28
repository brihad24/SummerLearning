instructions_number = int(input())
i = 1
shelf = list()

while i <= instructions_number:
    command = str(input())
    if command[0] == 'P':
        loaf = command[len(command)-1]
        shelf.append(loaf)
    
    if command[0] == 'B':
        shelf.pop(len(shelf)-1)
        
    print(shelf)
    if command[0] == 'C':
        loaf = command[len(command)-1]
        r = int(command[len(command)-3])
        l = int(command[len(command)-5])
        
        for a in range(r-1,l-1):
            if loaf == list[i]:
                print("1")
                
    i = i + 1