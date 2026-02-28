import tkinter as tk

# -------------------- Functions -------------------- #
def click(button_text):
    entry.insert(tk.END, button_text)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# -------------------- Main Window -------------------- #
root = tk.Tk()
root.title("Resizable GUI Calculator")
# Remove fixed size; user can resize freely
root.resizable(True, True)

# -------------------- Entry Box -------------------- #
entry = tk.Entry(root, font=('Arial', 28, 'bold'), borderwidth=3, relief="solid", justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# -------------------- Configure grid to expand -------------------- #
for i in range(4):  # 4 columns
    root.grid_columnconfigure(i, weight=1)
for i in range(6):  # 1 entry + 5 rows of buttons
    root.grid_rowconfigure(i, weight=1)

# -------------------- Buttons -------------------- #
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row_val = 1
col_val = 0

for button in buttons:
    if button == '=':
        b = tk.Button(root, text=button, bg="lightgreen", font=('Arial', 18, 'bold'),
                      command=calculate)
    else:
        b = tk.Button(root, text=button, bg="lightblue", font=('Arial', 18, 'bold'),
                      command=lambda bt=button: click(bt))
    b.grid(row=row_val, column=col_val, sticky="nsew", padx=3, pady=3)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# -------------------- Clear and Exit Buttons -------------------- #
tk.Button(root, text="C", bg="orange", font=('Arial', 18, 'bold'), command=clear)\
    .grid(row=row_val, column=0, sticky="nsew", padx=3, pady=3)

tk.Button(root, text="Exit", bg="red", fg="white", font=('Arial', 18, 'bold'), command=root.destroy)\
    .grid(row=row_val, column=1, columnspan=3, sticky="nsew", padx=3, pady=3)

# -------------------- Run the Window -------------------- #
root.mainloop()
