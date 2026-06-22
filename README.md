# 🏠 Land Rental Management System
A Python-based command-line application developed as part of the 
Fundamentals of Computing (CS4051NI) coursework at Islington College, 
London Metropolitan University.

## 📌 About
Techno Property Nepal is a CLI-based land rental system that allows 
users to rent and return land plots, track availability, and 
automatically generate invoices with fine calculation for late returns.

## ✨ Features
- Display available land plots with details (location, size, price)
- Rent land by selecting kitta number, anna, and duration
- Return land with automatic fine calculation for late returns
- Generate rental and return invoices
- Real-time update of land availability
- Exception handling for invalid inputs

## 🛠️ Technologies Used
- Python 3
- File Handling (read/write .txt files)
- Modular programming (4 separate Python modules)
- DateTime module for timestamps

## 📁 Project Structure

├── main.py        # Main program entry point

├── read.py        # Reads and displays land data

├── write.py       # Generates invoices

├── operation.py   # Handles rent and return logic

├── read.txt       # Land data file

## ▶️ How to Run
1. Make sure Python 3 is installed on your system
2. Clone the repository or download all files
3. Place all files in the same folder
4. Open terminal and navigate to the folder
5. Run the program:

## 📋 How to Use
1. View available land plots in the table
2. Enter your name and phone number
3. Choose an option:
   - **1** → Rent land
   - **2** → Return land
   - **3** → Exit
4. Follow the prompts to complete your transaction
5. Invoice is generated automatically

## ⚠️ Notes
- write.txt and return_invoice.txt are auto-generated on first run
- All land data is stored and updated in read.txt

## 👩‍💻 Author
Rojina Shrestha
Islington College | London Metropolitan University
