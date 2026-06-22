import datetime

def read_data():
    # Read land data from file
    file = open("read.txt","r")
    data = []
    for each in file:
        a = each.replace("\n","")
        data.append(a.split(","))
    return data

def display_table():
    data = read_data()
    
    print("Kitta   Location    Direction   Anna   Price     Availability")
    print("-" * 80)  # Separator line
    
    for row in data:
    # Define fixed widths for each column
        col1 = str(row[0])[:8].ljust(8)      # Left-align within 8 characters
        col2 = str(row[1])[:12].ljust(12)    # Left-align within 12 characters
        col3 = str(row[2])[:10].ljust(10)    # Left-align within 10 characters
        col4 = str(row[3])[:6].ljust(6)      # Left-align within 6 characters
        col5 = str(row[4])[:9].ljust(9)      # Left-align within 9 characters
        col6 = str(row[5])                    # No width specified for the last column
        
        # Concatenate columns with appropriate spacing
        row_formatted = col1 + col2 + col3 + col4 + col5 + col6
        
        # Print the formatted row
        print(row_formatted)

    print("~" * 80)
