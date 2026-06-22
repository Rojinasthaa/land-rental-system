def write_rent_invoice(name, phone_no, rented_lands, total_price):
    import datetime
    
    with open("write.txt", "w") as file:
        file.write("<Invoice>\n")
        file.write("Name: " + name + "\n")
        file.write("Phone No: " + phone_no + "\n")
        for rented_info in rented_lands:
            _, _, rented_date = rented_info  # Ignore unnecessary elements
            file.write("Rented Time: " + rented_date + "\n")
        file.write("\nTotal Price: " + str(total_price) + "\n")

def write_return_invoice(name, phone_no, return_lands):
    import datetime
    
    with open("return_invoice.txt", "w") as file:
        file.write("<Invoice>\n")
        file.write("Name: " + name + "\n")
        file.write("Phone No: " + phone_no + "\n")
        for returned_info in return_lands:
            kitta, duration, returned_date, fine, total = returned_info 
            file.write("Returned Time: " + returned_date + "\n")
            file.write("\nFine : " + str(fine) + "\n")
        file.write("\nTotal Price: " + str(total) + "\n")
