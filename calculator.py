# Import the necessary modules
import tkinter as tk

# Create the root window
root = tk.Tk()

# Added by Joseph Opio
def handle_digit(digit):
    # Get the current calculation string from the text entry field
    calculation = entry.get()

def handle_operation(operation, calculation=None):
    # Evaluate the calculation
    try:
        result = eval(calculation)
    except:
        result = "ERROR"

    # Update the result label with the result of the calculation
    result_label.configure(text=str(result))

    # Clear the text entry field
    entry.delete(0, tk.END)


# Create the text entry field
entry = tk.Entry(root)

# Create the result label
result_label = tk.Label(root, text="")

# Create the digit buttons
digit_button_0 = tk.Button(root, text="0", command=lambda: handle_digit(0))
digit_button_1 = tk.Button(root, text="1", command=lambda: handle_digit(1))
digit_button_2 = tk.Button(root, text="2", command=lambda: handle_digit(2))
digit_button_3 = tk.Button(root, text="3", command=lambda: handle_digit(3))
digit_button_4 = tk.Button(root, text="4", command=lambda: handle_digit(4))
digit_button_5 = tk.Button(root, text="5", command=lambda: handle_digit(5))
digit_button_6 = tk.Button(root, text="6", command=lambda: handle_digit(6))
digit_button_7 = tk.Button(root, text="7", command=lambda: handle_digit(7))
digit_button_8 = tk.Button(root, text="8", command=lambda: handle_digit(8))
digit_button_9 = tk.Button(root, text="9", command=lambda: handle_digit(9))

# Create the operation buttons
add_button = tk.Button(root, text="+", command=lambda: handle_operation("+"))
subtract_button = tk.Button(root, text="-", command=lambda: handle_operation("-"))
multiply_button = tk.Button(root, text="*", command=lambda: handle_operation("*"))
divide_button = tk.Button(root, text="/", command=lambda: handle_operation("/"))

# Set the layout

# Add the text entry field to the window
entry.grid(row=0, column=0, columnspan=3)

# Add the result label to the window
result_label.grid(row=5, column=0, columnspan=3)

# Add the digit buttons to the window
digit_button_0.grid(row=4, column=0)
digit_button_1.grid(row=3, column=0)
digit_button_2.grid(row=3, column=1)
digit_button_3.grid(row=3, column=2)
digit_button_4.grid(row=2, column=0)
digit_button_5.grid(row=2, column=1)
digit_button_6.grid(row=2, column=2)
digit_button_7.grid(row=1, column=0)
digit_button_8.grid(row=1, column=1)
digit_button_9.grid(row=1, column=2)

# Add the operation buttons to the window
add_button.grid(row=1, column=3)
subtract_button.grid(row=2, column=3)
multiply_button.grid(row=3, column=3)
divide_button.grid(row=4, column=3)

root.title("Calculator")
root.mainloop()