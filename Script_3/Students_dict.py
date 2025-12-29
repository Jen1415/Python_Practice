####################################################
class StudentsRecords:
    def __init__(self,filename):
        self.filename = filename




    def get_name_and_grade(self):
        name = input("Enter your name: ")
        while not((name.replace(" ","")).isalpha()):
            print("Error: Invalid Input. Name should contains letters only.")
            name = input("Enter your name: ")
        
        while True:
            try:
                grade = float(input("Enter your marks: "))
                if 0 <= grade <= 100:
                    break
                else:
                    print("Error: Invalid Input. Grade should be in range 0-100.")
            except ValueError:
                print("Error: Invalid Input. Grade should be a number.")
        
        grade = f"{grade:.2f}"

        return name,grade
    
    def record_student(self):
        name,grade = self.get_name_and_grade()
        with open(self.filename,"a") as f:
            f.write(f"{name},{grade}" +'\n')
        print("Student recorded succescfully.")

    def get_higher_achievers(self, threshold = 80):
        results = []
        with open(self.filename,"r") as f:
            for line in f:
                parts = line.strip().split(",")
                name = parts[0]
                grade = parts[1]
                if float(grade) > threshold:
                    results.append((name,grade))
                else:
                    continue
        return results


    def get_menu_choice(self):
        print("\n[1] Record new student")
        print("[2] Display student with grade > 80")
        print("[ ] Exit the program")
        return input("Enter your choice: ").strip()
        
####################################################

def main():
    records = StudentsRecords("Students_dict.txt")
    while True:
        choice = records.get_menu_choice()
        if choice == '1':
            records.record_student()
        elif choice == '2':
            students = records.get_higher_achievers()
            if students:
                print("Students with grade above 80:")
                for name,grade in records.get_higher_achievers():
                    print(f"{name} - {grade}")
            else:
                print("No students above 80.")
        else:
            print("Exiting the program...")
            exit()


main()
