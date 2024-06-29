from tkinter import Tk, Label, Entry, Button, StringVar, messagebox

def save_house_data():
    try:
        bhk1 = int(bhk1_var.get())
        footage1 = int(footage1_var.get())
        price1 = int(price1_var.get())
        
        bhk2 = int(bhk2_var.get())
        footage2 = int(footage2_var.get())
        price2 = int(price2_var.get())
        
        bhk3 = int(bhk3_var.get())
        footage3 = int(footage3_var.get())
        price3 = int(price3_var.get())
        
        with open("house_data.txt", "w") as file:
            file.write(f"{bhk1} {footage1} {price1}\n")
            file.write(f"{bhk2} {footage2} {price2}\n")
            file.write(f"{bhk3} {footage3} {price3}\n")
        
        messagebox.showinfo("Success", "Data saved successfully.")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

def clear_house_data():
    with open("house_data.txt", "w") as file:
        file.truncate()
    messagebox.showinfo("Success", "Data cleared successfully.")

DataFeedWindow = Tk()
DataFeedWindow.geometry("400x600")
DataFeedWindow.config(bg="lawn green")
DataFeedWindow.title("Housing Data Entry")

bhk1_var = StringVar()
footage1_var = StringVar()
price1_var = StringVar()

bhk2_var = StringVar()
footage2_var = StringVar()
price2_var = StringVar()

bhk3_var = StringVar()
footage3_var = StringVar()
price3_var = StringVar()

Label(DataFeedWindow, text="House 1 Details").grid(row=0, columnspan=2, pady=10)

Label(DataFeedWindow, text="BHKs:").grid(row=1, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=bhk1_var).grid(row=1, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Size:").grid(row=2, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=footage1_var).grid(row=2, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Price:").grid(row=3, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=price1_var).grid(row=3, column=1, padx=10, pady=5)

#Label(DataFeedWindow, text="------------------------").grid(row=4, columnspan=2, pady=10)

Label(DataFeedWindow, text="House 2 Details").grid(row=5, columnspan=2, pady=10)

Label(DataFeedWindow, text="BHKs:").grid(row=6, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=bhk2_var).grid(row=6, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Size:").grid(row=7, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=footage2_var).grid(row=7, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Price:").grid(row=8, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=price2_var).grid(row=8, column=1, padx=10, pady=5)

#Label(DataFeedWindow, text="------------------------").grid(row=9, columnspan=2, pady=10)

Label(DataFeedWindow, text="House 3 Details").grid(row=10, columnspan=2, pady=10)

Label(DataFeedWindow, text="BHKs:").grid(row=11, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=bhk3_var).grid(row=11, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Size:").grid(row=12, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=footage3_var).grid(row=12, column=1, padx=10, pady=5)

Label(DataFeedWindow, text="Price:").grid(row=13, column=0, padx=10, pady=5)
Entry(DataFeedWindow, textvariable=price3_var).grid(row=13, column=1, padx=10, pady=5)

Button(DataFeedWindow, text="Save Data", command=save_house_data).grid(row=14, columnspan=2, pady=10)
Button(DataFeedWindow, text="Clear Old Data", command=clear_house_data).grid(row=15, columnspan=2, pady=10)

DataFeedWindow.mainloop()
