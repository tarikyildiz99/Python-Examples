print("Enter first number:")
global firstNum 
firstNum = int(input())
print("Enter Second number:")
global secondNum 
secondNum = int(input())
def calculator():
    print("################")
    print("Choose an operator")
    print("1)+")
    print("2)-")
    print("3)x")
    print("4)/")
    operator = int(input())
    if operator == 1:
        answer = firstNum+secondNum
        print("Answer: "+str(answer))
    elif (operator == 2):
        answer = firstNum-secondNum
        print("Answer: "+str(answer))
    elif (operator == 3):
        answer = firstNum*secondNum
        print("Answer: "+str(answer))
    elif (operator == 4):
        answer = float(firstNum)/float(secondNum)
        print("Answer: "+str(answer))
    else:
        print("Error: Incorrect Number Given. Please Try Again")
        calculator()
calculator()
