import datetime
from read import read_data

def rent_land():
    lands = read_data()
    rented_list = []
    
    while True:
        try:
            kitta = input("Enter kitta no to rent land = ")
            found = False
        
            for land in lands:
                if kitta == land[0] and land[-1] == "Available":
                    anna_needed = int(input("Enter required no of anna = "))
                    if anna_needed == int(land[3]):
                        duration = int(input("Enter duration (months) = "))
                        rented_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                        rented_info = [kitta, duration, rented_date]
                        rented_list.append(rented_info)
                        land[-1] = "Not Available"
                        land.append(str(duration))
                        found = True
                        break
        
            if not found:
                print("Invalid kitta number or land not available.")
        
            cont = input("Do you want to continue (yes/no) = ").lower()
            if cont != "yes":
                break
        
        except:
            print("Invalid input. Please enter a valid kitta number.")
    
    # Update file with new availability
    with open("read.txt","w") as file:
        for land in lands:
            file.write(",".join(land) + "\n")
    
    return rented_list

def calculate_invoice(rented_list):
    lands = read_data()
    total_price = 0
    for rented in rented_list:
        for land in lands:
            if rented[0] == land[0]:
                total_price += int(land[4]) * rented[1]  # Price * Duration
    return total_price

def return_land():
    lands = read_data()  # Assuming read_data retrieves all land data including rental status
    return_list = []
    total = 0

    while True:
        kittaa = input("Enter kitta no of the land to be returned: ")
        found = False

        for land in lands:
            if kittaa == land[0] and land[-2] == "Not Available":
                land_returned = int(input("After how many months are you returning the land? "))
                returned_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # putting the value of rental duration in duration
                duration = int(land[-1])
                # checking if returned on time or delayed
                if land_returned <= duration :  # Check against original duration
                    print("Land returned on time.")
                    fine = 0
                else:
                    delay_months = land_returned -  duration
                    fine = (10/100)*(delay_months * int(land[4]))
                    print("Land returned with a delayed months. Fine will be applied.")
                total=total+fine
                # Update land availability and add return info to return_list
                land[-2] = "Available"
                returned_info = [land[0], duration, returned_date,fine, total]  # Update return details
                return_list.append(returned_info)

                found = True
                break

               
            else:
                print("Invalid kitta number or land cannot be returned or is already available.")
    
        cont = input("Do you want to continue returning lands (yes/no)? ").lower()
        if cont != "yes":
            break

    # Update file with updated availability
    with open("read.txt", "w") as file:
        for land in lands:
            if land[0] == kittaa and land[-2] == "Available":
                # If this is the returned land, write all columns except the duration
                file.write(",".join(land[:-1]) + "\n")
            else:
                # For other lands, write the full line
                file.write(",".join(land) + "\n")
            
    return return_list
