# Hakan İleri

def default():      # default solution 
    numRange   = 5
    oddList    = list(range(1,numRange+1,2))
    evenList   = list(range(0,numRange+1,2))
    merge_and_print(oddList,evenList)

def user_input():   # solution with user input
    # Create a list with odd numbers ranging from zero to user input 
    print("\nType range for odd numbered list:")
    oddInput   = get_input()
    oddList    = list(range(1,int(oddInput)+1,2))
    # Create a list with even numbers ranging from zero to user input 
    print("\nType range for even numbered list:")
    evenInput  = get_input()
    evenList   = list(range(0,int(evenInput)+1,2))
    merge_and_print(oddList,evenList)

def get_input():    # get input from user and check if the input is an integer or not
    inputNum = input()   
    while inputNum.isdigit() == False:
        print("\nIllegal input! Enter an integer: ")
        inputNum = input()
    return inputNum

def merge_and_print(oddList,evenList):
    # Merge and print odd and even lists 
    mergedList = oddList + evenList #merge lists with concatenation method
    mergedList = [element * 2 for element in mergedList] # multiply list elements by 2
    print("\nMerged list after multiplying by 2:")
    for i in mergedList:
        print(i,"Data type:",type(i))
    return(mergedList)    

def choicer():
    user_choice = (input("\nType 'default' for default list / 'input' for list with user input / 'quit' to quit: "))
    if user_choice =="default":
        default()
    elif user_choice =="input":
        user_input()
    elif user_choice =="quit":
        exit
    else:
        print("Wrong input!\n")    
        choicer()

choicer()        