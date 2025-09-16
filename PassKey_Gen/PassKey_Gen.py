from random import *
from tkinter import *

# Input for Password
num = "0123456789"
alphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'!@#$%&_+-():;?/"

# Generation Function
def Create_Pass():
    TheChoice = Tchoice.get()
    
    if TheChoice == "":
        resultbox.config(text="Select the type of password you'd like")
        return

    length = int(pass_length.get())
    randpass = []
    for i in range(length):
        randpass.append(choice(TheChoice))
        
    result = "".join(randpass)
    TheResult = "Your Password: {result}"
    resultbox.config(text=TheResult)

# Copy function
def Copy():
    text_to_copy = resultbox.cget("text").replace("Your Password: ", "")  # Get the text from resultbox and remove the prefix
    if text_to_copy:  # Ensure there's text to copy
        window.clipboard_clear()  # Clear the clipboard
        window.clipboard_append(text_to_copy)  # Append the text to the clipboard
    if text_to_copy and "Your Password:" in text_to_copy:
        text_to_copy = text_to_copy.replace("Your Password: ", "")
    else:
        return  # Do nothing if no valid password is present
    window.update()  # Update the clipboard


# GUI for Random Pass Gen
window = Tk()
window.geometry("800x500")
window.title("Random Pass Generator")

# Background Image
background_label = Label(window, bg="white")  # Changed background to white
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Main Title
ProgName = Label(window, 
                 text="Password Generator", 
                 font=("Poppins", 20, 'bold'), 
                 fg="black",  # Changed text color to black
                 bg="white")  # Changed background to white
ProgName.place(relx=0.5, rely=0.1, anchor="center")

# Password Type Selection
ChooseType = Label(window,
                   text="Choose a type:",
                   font=("Poppins", 15, 'bold'),
                   fg="black",  # Changed text color to black
                   bg="white")  # Changed background to white
ChooseType.place(relx=0.1, rely=0.2)

Tchoice = StringVar()
NumChoice = Radiobutton(window,
                        text="Numeric",
                        font=("Poppins", 12),
                        variable=Tchoice,
                        value=num,
                        fg="black",  # Changed text color to black
                        bg="white",  # Changed background to white
                        selectcolor="white")  # Changed select color to white
AlphaNumChoice = Radiobutton(window,
                            text="Alphanumeric",
                            font=("Poppins", 12),
                            variable=Tchoice,
                            value=alphanum,
                            fg="black",  # Changed text color to black
                            bg="white",  # Changed background to white
                            selectcolor="white")  # Changed select color to white
SpecialNumChoice = Radiobutton(window,
                              text="Special",
                              font=("Poppins", 12),
                              variable=Tchoice,
                              value=spalphanum,
                              fg="black",  # Changed text color to black
                              bg="white",  # Changed background to white
                              selectcolor="white")  # Changed select color to white

NumChoice.place(relx=0.1, rely=0.3)
AlphaNumChoice.place(relx=0.1, rely=0.35)
SpecialNumChoice.place(relx=0.1, rely=0.4)

# Password Length
Size = Label(window,
            text="Length:",
            font=("Poppins", 15, 'bold'),
            fg="black",  # Changed text color to black
            bg="white")  # Changed background to white
Size.place(relx=0.68, rely=0.28)

pass_length = Spinbox(window,
                     from_=8,
                     to=100,
                     font=("Poppins", 12),
                     width=5)
pass_length.place(relx=0.8, rely=0.29)

# Generate Button
GenButton = Button(window,
                  text="Generate",
                  command=Create_Pass,
                  font=("Poppins", 12),
                  bg="cyan",
                  fg="black", width=15)
GenButton.place(relx=0.20, rely=0.55)

#Copy Button
CpyButton = Button(window,
                  text="Copy",
                  command= Copy,
                  font=("Poppins", 12),
                  bg="cyan",
                  fg="black", width=15)
CpyButton.place(relx=0.60, rely=0.55)

# Result Display
resultbox = Label(window,
                 font=("Poppins", 14),
                 fg="black",  # Changed text color to black
                 bg="white",  # Changed background to white
                 wraplength=600)
resultbox.place(relx=0.5, rely=0.75, anchor="center")

# Make resultbox selectable
resultbox.config(text="Your Password will appear here", anchor="center", justify="center")  # Added default text
resultbox.bind("<Button-1>", lambda e: resultbox.focus_set())  # Allow focus on click

window.mainloop()