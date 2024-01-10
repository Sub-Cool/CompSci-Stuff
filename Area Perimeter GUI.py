import tkinter as tk

def calculate_area():
    length = float(length_entry.get())
    width = float(width_entry.get())
    area = length * width
    result_label.config(text=f"Area: {area}")

def calculate_perimeter():
    length = float(length_entry.get())
    width = float(width_entry.get())
    perimeter = 2 * (length + width)
    result_label.config(text=f"Perimeter: {perimeter}")

# Create the main window
window = tk.Tk()
window.title("Area/Perimeter Calc")
window.geometry("600x400")  # Set the window size to 600x400

# Set the background color
window.configure(bg="#4B0082")  # Purple color

# Create the input labels and entry fields
length_label = tk.Label(window, text="Length:")
length_label.pack(pady=10)  # Add padding between labels
length_entry = tk.Entry(window)
length_entry.pack()

width_label = tk.Label(window, text="Width:")
width_label.pack(pady=10)  # Add padding between labels
width_entry = tk.Entry(window)
width_entry.pack()

# Create the buttons for calculating area and perimeter
area_button = tk.Button(window, text="Calculate Area", command=calculate_area)
area_button.pack(pady=5)  # Add padding between buttons
perimeter_button = tk.Button(window, text="Calculate Perimeter", command=calculate_perimeter)
perimeter_button.pack(pady=5)  # Add padding between buttons

# Create the label for displaying the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()