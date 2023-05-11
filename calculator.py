def operations(val, var):

    #Arithmetic part
    val = int(input("Enter a number: "))
    op = str(input("Enter an operation symbol: [ +, -, *, /, //, **, % ]: "))
    var = int(input("Enter a number: "))

    symbols = {

    #Operations ahead of output
    #Include commas
        "+": val + var,
        "-": val - var,
        "*": val * var,
        "/": val / var,
        "//": val // var,
        "**": val ** var,
        "%": val % var

    }

#Conditions the dictionary keys and calls them
    if op in symbols:
        print(f"Result: {symbols[op]}")
    else:
        print("Invalid operator.")

operations(int, int) #Cals the types.

def main():

    while True: #Infinite loop
        opt = str(input("Would you like to start a new session? (y/n): ")).lower()
    
        if opt == "y":
            operations(None, None) #Repeats the calling of operations()
        elif opt == "n":
            print("Bye!")
            break #End of iteration
        else:
            #To notify that the questions will be asked again.
            print("Invalid option, reformulating question...")

main() #Final verification to see if starting a session is required.