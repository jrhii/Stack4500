#################################
# Authors: Tarik Muzughi, Jim Harter
#
# Description: Allows a user to create a stack and perform operations on it
# The stack used is a realistic implementation using Dictionaries, and has
# the same pros and cons and functional applications of a real stack
#################################

MAX_STACK_LEN = 12

#Creates a new stack
def NewStack(): 
    return {
        "value": None,
        "below": None
    }

#true if stack is empty
def isEmpty(Stack):
    return Stack["below"] == None

#pushed onto a stack and returns the new stack.  Does not mutate the given stack
def pushStack(Stack, value):
    return {
        "value": value,
        "below": Stack
    }

#returns the stack under the top.  Not that this does not return the value of the top,
# nor does it mutate the provided stack
def popStack(Stack):
    if isEmpty(Stack):
        print("bad")
        quit()
    return Stack["below"]

#returns the value of the top of the stack
def top(Stack):
    if isEmpty(Stack):
        print("bad")
        quit()
    return Stack["value"]

#makes sure that Stack has the same state at end of function
def stackLen(Stack):
    reverseStack = NewStack()
    length = 0

    while isEmpty(Stack) != True:
        reverseStack = pushStack(reverseStack, top(Stack))
        Stack = popStack(Stack)
        length = length + 1

    while isEmpty(reverseStack) != True:
        Stack = pushStack(Stack, top(reverseStack))
        reverseStack = popStack(reverseStack)

    return length


def displayStack(Stack):
    print("Stack Contents:")
    reverseStack = NewStack()

    while isEmpty(Stack) != True:
        print(top(Stack))
        reverseStack = pushStack(reverseStack, top(Stack))
        Stack = popStack(Stack)

    while isEmpty(reverseStack) != True:
        Stack = pushStack(Stack, top(reverseStack))
        reverseStack = popStack(reverseStack)


userIn = input("1. Create Stack\n2. isEmpty\n3. push\n4. pop\n5. top:\n6. exit\n")
userStack = None

while userIn is not "6":
    #create stack
    if userIn == "1":
        userStack = NewStack()
    #exit
    elif userIn == "6":
        continue
    elif userStack == None:
        userIn = input("ERROR, No stack exists!\n1. Create Stack\n2. isEmpty\n3. push\n4. pop\n5. top\n6. exit\n")
        continue
    #check if empty
    elif userIn == "2":
        if isEmpty(userStack):
            print("The stack is empty")
        else:
            print("The stack is not empty")
    #Push onto stack
    elif userIn == "3":
        if stackLen(userStack) >= MAX_STACK_LEN:
            print("ERROR: max stack length of %d achieved." % (MAX_STACK_LEN))
        else:
            pushIn = input("Enter a character to push")
            while len(pushIn) is not 1:
                pushIn = input("ERROR: Enter a SINGLE character to push\n")
            
            userStack = pushStack(userStack, pushIn)
    #Pop from stack
    elif userIn == "4":
        userStack = popStack(userStack)
    #show top of stack
    elif userIn == "5":
        topChar = top(userStack)
        print("The top of the stack is %s" % (topChar))
    #default
    else:
        userIn = input("ERROR, Invalid Input!\n1. Create Stack\n2. isEmpty\n3. push\n4. pop\n5. top\n6. exit\n")
        continue
    
    displayStack(userStack)
    userIn = input("1. Create Stack\n2. isEmpty\n3. push\n4. pop\n5. top:\n6. exit\n")

print("done")