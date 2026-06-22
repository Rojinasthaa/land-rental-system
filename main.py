from read import display_table
from operation import rent_land, calculate_invoice, return_land
from write import write_rent_invoice, write_return_invoice

def intro():
    print("\n" + "."*79)
    print("\t\t Welcome to Techno Property Nepal")
    print("."*80)
    print("\t\t\tLalitpur, Nepal")
    print("\t\tContact no: 9745304606")
    print("\t\tEmail: techno_property@gmail.com")
    print("\n")
intro()


       
def handle_choice(choice, name, phone_no):
    if choice == "1":
        rented_lands = rent_land()
        total_price = calculate_invoice(rented_lands)
        print("\n","*"*79)
        print("\t\t\t<<<Invoice>>>")
        print("-" * 80)
        print("Name: " + name)
        print("Phone No: " + phone_no)
        for rented_info in rented_lands:
            _, _, rented_date = rented_info  # Extract rented_date
            print("Rented Time: " + rented_date)
        print("Total Price: " + str(total_price))
        print("*"*80)
        print("\n")
        write_rent_invoice(name, phone_no, rented_lands, total_price)
        display_table()
         
    elif choice == "2":
        return_lands = return_land()
        print("\n","*"*79)
        print("\t\t\t<<<Return Invoice>>>")
        print("-" * 80)
        print("Name: " + name)
        print("Phone No: " + phone_no)
        for returned_info in return_lands:
            kitta, duration, returned_date, fine, total = returned_info
            print("Returned Time: " + returned_date) 
            print("Fine : " + str(fine) + "\n")
        print("\nTotal price  : " + str(total))
        print("*"*80)
        print("\n")
        write_return_invoice(name, phone_no, return_lands)
        display_table()
        
    elif choice == "3":
        print("Exiting...")
        
    else:
        print("Choose a valid option.")
        
def taking_inputs():
    display_table()
    name = input("Please enter your name: ")
    phone_no = input("Enter phone number: ")
    while True:
        print("\nChoose your option")
        print("-" * 20)
        print("Enter 1 to rent the land")
        print("Enter 2 to return the land")
        print("Enter 3 to exit\n")
        
        choice = input("Enter your choice: ")
        
        if choice in ("1", "2", "3"):
            handle_choice(choice, name, phone_no)
            if choice == "3":
                break
        else:
            print("Invalid choice. Please choose a valid option (1, 2, or 3).")
    
taking_inputs()


