def get(x):
    result = ''
    if x % 3==0: result +='G' 
    if x % 5==0: result +='N'
    return result if result else num

print("Select operation.")
print("1. \GET")
print("2. Exit")


while True:
    # take input from the user
    choice = input("Enter choice(1/2): ")
    if choice in ('1'):
        num = int(input("Enter an integer number: "))
        print('The Result is :', get(num))
        next_calculation = input("Let's try another number? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
        break