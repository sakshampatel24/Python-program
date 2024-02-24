first = input("enter the number : ")
operator = input("enter operator (+,-,*,/,%) : ")
second = input("enter the number : ")
first = int(first)
second = int(second)
if operator == "+" :
        print(first + second)
elif operator == "-" :
          print(first - second)
elif operator == "*" :
           print(first * second)
elif operator == "/" :
            print(first / second)
elif operator == "%" :
            print(first % second)
else:
            print("Invalid operator")