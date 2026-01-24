

while True:
    num = int(input("Enter a number: "))
    if num % 2 == 0 :
        continue
    elif num == -999:
        break
    else:
        print("The incremented number is", (num+ 1))