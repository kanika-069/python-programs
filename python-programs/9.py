record={}
while True:
    key=input("What is your name:")
    val=int(input("What is your bid?: $"))
    record[key]=val
    userInput=input("Are there any other bidders? Type 'yes' or 'no' .\n    ")
    maxVal=val
    maxKey=key
    if userInput=='no':
        for i in record:
            if record[i]>maxVal:
                maxVal=record[i]
                maxKey=i
        print("The winner is "+maxKey+" with a bid of $"+str(maxVal))
        break
    elif userInput=='yes':
        continue
    else:
        break