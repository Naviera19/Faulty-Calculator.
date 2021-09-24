'''Design a calculator using Python which can solve all problems other than 45*3=555, 56+9=77, 56/6=4. 
The calculator must keep on calculating according to the user's commands. 
I've used while loop with break and continue statements'''

while(True):
    print("Enter the no. 1: ")
    v1 = int(input())
    print("Enter the no. 2: ")
    v2 = int(input())
    print("Enter the operator: ")
    v3 = input()

    if v1 == 45 and v2 == 3 and v3 == '*':
        print("555")
    elif v1 == 56 and v2 == 9 and v3 == '+':
        print("77")
    elif v1 == 56 and v2 == 6 and v3 == '/':
        print("4")
    elif v3 == '*':
        print(int(v1) * int(v2))
    elif v3 == '+':
        print(int(v1) + int(v2))
    elif v3 == '-':
        print(int(v1) - int(v2))
    elif v3 == '/':
        print(int(v1) / int(v2))
    elif v3 == '%':
        print(int(v1) % int(v2))
    else:
        print("Sorry! This isn't right.")

    ques = input("Do you want to calculate again? Type Y or N.")
    if ques == 'Y':
        continue
    if ques == 'N':
        print("You exited.")
        break
