import tkinter as tk

root = tk.Tk()
root.title('Calculator')

# Dictionary to store grid location and functionality of each operator
op_dict = {'÷':(1, 1, lambda x,y:x/y),
           '×':(1, 2, lambda x,y:x*y),
           '-':(2, 3, lambda x,y:x-y),
           '+':(3, 3, lambda x,y:x+y),
           '%':(5, 0, lambda x,y:(x*y)/100)}
operation_type = 0 # default value to protect against improper use of '=' button

# Numeral click functionality: display numeral input on screen
def num_click(x):
    current = screen.get()
    screen.delete(0, tk.END)
    screen.insert(0, current + str(x))

# Operator click functionality: store numerical input and subsequent operation
def op_click(x):
    global number_1
    global operation_type
    if screen.get() == '':
        return
    number_1 = float(screen.get())
    operation_type = x
    screen.delete(0, tk.END)

# Equals click functionality: access stored input and operation, compute output and display on screen
def equals():
    global operation_type
    if operation_type == 0:
        return
    number_2 = float(screen.get())
    operation = op_dict[operation_type][2]
    operation_type = 0
    result = operation(number_1, number_2)
    screen.delete(0, tk.END)
    screen.insert(0, f'{result:g}')

# Adding display screen
screen = tk.Entry(root, width=40, borderwidth=5)
screen.grid(row=0, column=0, columnspan=4)

# Adding numeral buttons
for i in range(9):
    button = tk.Button(root, text=str(i+1), width=10, height=4, command=lambda i=i: num_click(str(i+1)))
    r = 4-i//3
    c = i%3
    button.grid(row=r, column=c)
tk.Button(root, text='0', width=10, height=4, command=lambda: num_click(0)).grid(row=5, column=1)

# Adding operator buttons
for op in op_dict.keys():
    button = tk.Button(root, text=op, width=10, height=4, command=lambda op=op: op_click(op))
    button.grid(row=op_dict[op][0], column=op_dict[op][1])

# Adding other buttons
tk.Button(root, text='C', width=10, height=4, command=lambda: screen.delete(0, tk.END)).grid(row=1, column=0)
tk.Button(root, text='⌫', width=10, height=4, command=lambda: screen.delete(screen.index(tk.END)-1)).grid(row=1, column=3)
tk.Button(root, text='.', width=10, height=4, command=lambda: num_click('.')).grid(row=5, column=2)
tk.Button(root, text='=', width=10, height=8, command=equals).grid(row=4, column=3, rowspan=2)

root.mainloop()