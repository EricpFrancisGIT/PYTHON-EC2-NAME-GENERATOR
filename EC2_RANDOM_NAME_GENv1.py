import random
import string


def generate_unique_name(length=7):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

#Main Script
def main():
    print('Welcome to the Level-Up Corporation Instance Name Generator!')
    print('----------------FOR AUTHORIZED DEPARTMENTS ONLY----------------')
    
    num_instances = (input("How many instances do you need names for?")).strip()
    try:
        num_instances = int(num_instances)
        if num_instances <= 0:
            print('Incorrect. Please enter a positive number for instances')
            return
    except ValueError:
        print('Input Invalid. Enter a number for instances')
        return

    department = str(input('Please state the name of the departmant(Marketing Dept, Accounting Dept, Fin-Ops Dept)'))

    acceptable_departments = ["Marketing", "Accounting", "Fin-Ops"]
    if department not in acceptable_departments:
        print('Error, Your department is not authorized to use this Name Generator!')
        return

    
    print("\nGenerating instances names for the department:")
    for _ in range(num_instances):
        unique_id = generate_unique_name()
        EC2_instance_name = f"{department}-{unique_id}"
        print(EC2_instance_name)

if __name__ == "__main__":
    main()

    print("Thank you for using the Level-Up Corporate EC2 Instance Name Generator. Goodbye!")
