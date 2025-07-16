import os
from datetime import datetime

def clear_screen():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calculator():
    while True:
        clear_screen() 

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        print("╔════════════════════════════════════════════╗")
        print('║           Welcome to Calculator            ║')
        print("╠════════════════════════════════════════════╣")
        print(f"║       Date & Time: {now}     ║" )
        print("╠════════════════════════════════════════════╣")
        print('║ 1. Addition (+)                            ║')
        print('║ 2. Subtract (-)                            ║')
        print('║ 3. Multiply (*)                            ║')
        print('║ 4. Divide   (/)                            ║')
        print('║ 5. Exit     ...                            ║')
        print("╚════════════════════════════════════════════╝")

        choice = input('Enter Your Choice (1-5): ')

        if choice == '5':
            print("Thank you for using the calculator. Goodbye...!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                input("Press Enter to continue...")
                continue

            if choice == '1':
                result = num1 + num2
                print("Result:", result)
            elif choice == '2':
                result = num1 - num2
                print("Result:", result)
            elif choice == '3':
                result = num1 * num2
                print("Result:", result)
            elif choice == '4':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                else:
                    result = num1 / num2
                    print("Result:", result)
        else:
            print("Invalid choice. Please select from 1 to 5.")

        input("Press Enter to continue...")

calculator()
