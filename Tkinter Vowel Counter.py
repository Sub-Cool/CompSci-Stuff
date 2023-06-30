import tkinter
import tkinter.messagebox

# Create the VowelCounterGUI class
class VowelCounterGUI:
    def __init__(self):
        # Create the main window
        self.main_window = tkinter.Tk()

        # Create the frames
        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()

        # Create the widgets for the top frame
        self.prompt_label = tkinter.Label(self.top_frame, text="Enter a string: ")
        self.string_entry = tkinter.Entry(self.top_frame, width=10)

        # Pack the top frame's widgets
        self.prompt_label.pack(side="left")
        self.string_entry.pack(side="left")

        # Create the widgets for the bottom frame
        self.vowel_button = tkinter.Button(self.bottom_frame, text="Count Vowels", command=self.count_vowels)

        # Pack the bottom frame's widgets
        self.vowel_button.pack()

        # Pack the frames
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the main loop
        tkinter.mainloop()

    # The count_vowels method is the callback function for the Count Vowels button
    def count_vowels(self):
        # Get the string from the user
        user_string = self.string_entry.get()

        # Initialize the vowel counter
        vowel_count = 0

        # Initialize the vowel counters
        a_count = 0
        e_count = 0
        i_count = 0
        o_count = 0
        u_count = 0

        # Loop through the string
        for letter in user_string:
            # Check if the letter is a vowel
            if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
                # Increment the vowel counter
                vowel_count += 1

                # Increment the vowel counters
                if letter == "a":
                    a_count += 1
                elif letter == "e":
                    e_count += 1
                elif letter == "i":
                    i_count += 1
                elif letter == "o":
                    o_count += 1
                elif letter == "u":
                    u_count += 1

        # Display the results in a message box
        tkinter.messagebox.showinfo("Vowel Counter", "There are " + str(vowel_count) + " vowels in the string.\nThere are " + str(a_count) + " a's in the string.\
        \nThere are " + str(e_count) + " e's in the string.\nThere are " + str(i_count) + " i's in the string.\nThere are " + str(o_count) + " o's in the string.\
        \nThere are " + str(u_count) + " u's in the string.")

# Create an instance of the VowelCounterGUI class
vowel_counter = VowelCounterGUI()
