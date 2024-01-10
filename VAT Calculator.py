import tkinter as tk

def calculate_vat():
    prices = [float(entry.get()) for entry in price_entries]
    vat_percentage = float(vat_entry.get()) / 100
    vat = sum(prices) * vat_percentage
    result_label.config(text=f"VAT: {vat}")

def calculate_total():
    prices = [float(entry.get()) for entry in price_entries]
    vat_percentage = float(vat_entry.get()) / 100
    vat = sum(prices) * vat_percentage
    total = sum(prices) + vat
    result_label.config(text=f"Total: {total}")

# Create the main window
window = tk.Tk()
window.title("VAT Calculator")
window.geometry("900x600")  # Set the window size to 900x600

# Set the background color
window.configure(bg="#8B0000")  # Set the background color to dark red (#8B0000)

# Create the input labels and entry fields
price_labels = []
price_entries = []

num_items = int(input("Enter the number of items: ")) # User must enter this in the command line
for i in range(num_items):
    label = tk.Label(window, text=f"Price {i+1} (in pounds.pence):")
    label.pack(pady=10)  # Add padding between labels
    price_labels.append(label)
    entry = tk.Entry(window)
    entry.pack()
    price_entries.append(entry)

vat_label = tk.Label(window, text="VAT percentage:")
vat_label.pack(pady=10)  # Add padding between labels
vat_entry = tk.Entry(window)
vat_entry.pack()

# Create the buttons for calculating VAT and total
vat_button = tk.Button(window, text="Calculate VAT", command=calculate_vat)
vat_button.pack(pady=5)  # Add padding between buttons
total_button = tk.Button(window, text="Calculate Total", command=calculate_total)
total_button.pack(pady=5)  # Add padding between buttons

# Create the label for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
