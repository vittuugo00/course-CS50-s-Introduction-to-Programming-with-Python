    # ask user for their name
    #python documentation https://docs.python.org/
    #

name = input("whats your name? ")

# remove whitespaces from str
name = name.strip() 

# capitalize user's name
name = name.title()

if(name.split()): 
    first, second = name.split()


print("hello!", first)

print("hello \"friend\"")