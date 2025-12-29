class NameAge:
    def __init__(self,filename):
        self.filename = filename


    def write_in_file(self, info):
        info = ",".join(info)
        with open(self.filename, "a") as f:
            f.write(info + '\n')

    def take_name_and_age(self):

        name = input("Enter your name: ")
        while not((name.replace(" ","")).isalpha()):
            print("Error: Invalid Input. Name should contains letters only.")
            name = input("Enter your name: ")
        


        while True:
            try:
                age = int(input("Enter your age: "))
                if age < 0 or age > 150:
                    print("Error: Invalid Input. Your age is out of range.")
                    continue
                break
            except ValueError:
                print("Error: Invalid Input. Age should be an integer.")

        return [name,str(age)]

def main():
    na = NameAge("Name_Age.txt")
    na.write_in_file(na.take_name_and_age())
    print("Action Successfully")

main()
    
