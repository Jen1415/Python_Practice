def take_name_and_age():
    info = []
    name = input("Enter your name: ")
    while not((name.replace(" ","")).isalpha()):
        print("Error: Invalid Input. Name should contains letters only.")
        name = input("Enter your name: ")
    
    info.append(name)

    while True:
        try:
            age = int(input("Enter your age: "))
            if age < 0 or age > 150:
                print("Error: Invalid Input. Your age is out of range.")
                continue
            break
        except ValueError:
            print("Error: Invalid Input. Age should be an integer.")

    info.append(str(age))

    return info

def main():
    userInput = take_name_and_age()
    userInfo = ",".join(userInput)
    with open("Name_Age.txt","a") as f:
        f.write(userInfo)
        f.write("\n")
    print("Action Successfully")    


main()
    
