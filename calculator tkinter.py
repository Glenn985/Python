import tkinter as tk


def update_display(value):
    current_text = display_var.get()
    display_var.set(current_text + value)

sai = tk.Tk()
sai.title("Calculator")
sai.geometry("400x500")



# Label to display the calculator input
display_var = tk.StringVar()
display_label = tk.Label(sai, textvariable=display_var, font=('Arial', 24), anchor='e', relief='sunken', bd=5)
display_label.pack(fill='both', expand=True)



def getnumber():
    global operator, firstnumber, number
    
    display_text = display_var.get()
    
    if '+' in display_text:
        operator = '+'
        firstnumber, number = map(int, display_text.split('+'))
    elif '-' in display_text:
        operator = '-'
        firstnumber, number = map(int, display_text.split('-'))
    elif '*' in display_text:
        operator = '*'
        firstnumber, number = map(int, display_text.split('*'))
    elif '/' in display_text:
        operator = '/'
        firstnumber, number = map(int, display_text.split('/'))
    else:
        # No operator found
        firstnumber = int(display_text)
    
    # Perform calculation if an operator is detected
    if operator:
        if operator == "+":
            answer = firstnumber + number
        elif operator == "-":
            answer = firstnumber - number
        elif operator == "*":
            answer = firstnumber * number
        elif operator == "/":
            if number != 0:
                answer = firstnumber / number
            else:
   
                answer = "Error"
        
        
        display_var.set(str(answer))
      
        
        # Reset variables for the next calculation
        operator = ""
        firstnumber = 0
        number = 0



# Frame to hold the buttons
button_frame = tk.Frame(sai)
button_frame.pack(fill='both', expand=True)

# Create buttons for numbers 0 to 9 and arithmetic operations
button0 = tk.Button(button_frame, text='0', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('0'))
button0.grid(row=4, column=1, sticky='nsew', padx=5, pady=5)

button1 = tk.Button(button_frame, text='1', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('1'))
button1.grid(row=3, column=0, sticky='nsew', padx=5, pady=5)

button2 = tk.Button(button_frame, text='2', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('2'))
button2.grid(row=3, column=1, sticky='nsew', padx=5, pady=5)

button3 = tk.Button(button_frame, text='3', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('3'))
button3.grid(row=3, column=2, sticky='nsew', padx=5, pady=5)

button4 = tk.Button(button_frame, text='4', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('4'))
button4.grid(row=2, column=0, sticky='nsew', padx=5, pady=5)

button5 = tk.Button(button_frame, text='5', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('5'))
button5.grid(row=2, column=1, sticky='nsew', padx=5, pady=5)

button6 = tk.Button(button_frame, text='6', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('6'))
button6.grid(row=2, column=2, sticky='nsew', padx=5, pady=5)

button7 = tk.Button(button_frame, text='7', font=('Arial', 18), padx=20, pady=20, command=lambda:update_display('7'))
button7.grid(row=1, column=0, sticky='nsew', padx=5, pady=5)

button8 = tk.Button(button_frame, text='8', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('8'))
button8.grid(row=1, column=1, sticky='nsew', padx=5, pady=5)

button9 = tk.Button(button_frame, text='9', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('9'))
button9.grid(row=1, column=2, sticky='nsew', padx=5, pady=5)

button_plus = tk.Button(button_frame, text='+', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('+'))
button_plus.grid(row=4, column=2, sticky='nsew', padx=5, pady=5)

button_minus = tk.Button(button_frame, text='-', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('-'))
button_minus.grid(row=4, column=0, sticky='nsew', padx=5, pady=5)

button_multiply = tk.Button(button_frame, text='*', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('*'))
button_multiply.grid(row=2, column=3, sticky='nsew', padx=5, pady=5)

button_divide = tk.Button(button_frame, text='/', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('/'))
button_divide.grid(row=3, column=3, sticky='nsew', padx=5, pady=5)

button_equal = tk.Button(button_frame, text='=', font=('Arial', 18), padx=20, pady=20, command=lambda:getnumber())
button_equal.grid(row=5, column=0, sticky='nsew', padx=5, pady=5)  # Corrected column value


button_decimal = tk.Button(button_frame, text='.', font=('Arial', 18), padx=20, pady=20, command=lambda: update_display('.'))
button_decimal.grid(row=4, column=3, sticky='nsew', padx=5, pady=5)









