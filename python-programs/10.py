# calculator

def calculation():
    firstNum=int(input("What's the first number?: "))
    print("+")
    print("-")
    print("*")
    print("/")
    op= input("Pick an operation:  ")
    secondNum=int(input("What's the next number?: "))
    if op=="+":
            output=firstNum+secondNum
            print(f"{firstNum} + {secondNum} = {output}")
    elif op=="-":
            output=firstNum-secondNum
            print(f"{firstNum} - {secondNum} = {output}")
    elif op=="*":
            output=firstNum*secondNum
            print(f"{firstNum} * {secondNum} = {output}")
    elif op=="/":
            output=firstNum/secondNum
            print(f"{firstNum} / {secondNum} = {output}")
    else:
            output=0.0
            print(f"{firstNum} undefined {secondNum} = {output}")
    return output

def cal1(output):
           print("+")
           print("-")
           print("*")
           print("/")
           op= input("Pick an operation:  ")
           secondNum=int(input("What's the next number?: "))
           if op=="+":
               output1=output+secondNum
               print(f"{output} + {secondNum} = {output1}")
           elif op=="-":
               output1=output-secondNum
               print(f"{output} - {secondNum} = {output1}")
           elif op=="*":
               output1=output*secondNum
               print(f"{output} * {secondNum} = {output1}")
           elif op=="/":
               output1=output/secondNum
               print(f"{output} / {secondNum} = {output1}")
           else:
               output1=0.0
               print(f"{output} undefined {secondNum} = {output1}")
            

k=calculation()
while True:
    userInput=input(f"Type 'y' to continue calculating with {k}, or type 'n' to start a new calculation:  " )
    if userInput=="y":
           k=cal1()
    else:
          k=calculation()