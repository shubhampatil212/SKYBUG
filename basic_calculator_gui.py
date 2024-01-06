import tkinter as tk

large_font = ("Verdana", 40, "bold")
small_font = ("Verdana", 16)
digits_font = ("Verdana", 18, "bold")  # Adjusted the font size for digits
default_font = ("Verdana", 20)
off_white_color = "#F0F0F0"
white_color = "#FFFFFF"
light_blue_color = "#87CEFA"
light_gray_color = "#D3D3D3"
label_color = "#800080"

class CustomCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("375x667")
        self.root.resizable(0, 0)
        self.root.title("My Custom Calculator")
        self.total_exp = ""
        self.current_exp = ""
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        # Buttons and operators
        self.digits = {7: (1, 1), 8: (1, 2), 9: (1, 3), 4: (2, 1), 5: (2, 2), 6: (2, 3),
                       1: (3, 1), 2: (3, 2), 3: (3, 3), 0: (4, 2), '.': (4, 1)}
        self.operations = {'/': '\u00F7', '*': '\u00D7', '-': '-', '+': '+'}

        self.buttons_frame = self.create_buttons_frame()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

        self.bind_keys()

    def create_display_frame(self):
        frame = tk.Frame(self.root, height=221, bg=light_gray_color)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_exp, anchor=tk.E, bg=light_gray_color,
                               fg=label_color, padx=24, font=small_font)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_exp, anchor=tk.E, bg=light_gray_color,
                         fg=label_color, padx=24, font=large_font)
        label.pack(expand=True, fill='both')

        return total_label, label

    def add_to_expression(self, value):
        self.current_exp += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=white_color, fg=label_color,
                               font=digits_font, borderwidth=0, height=2,
                               command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_exp += operator
        self.total_exp += self.current_exp
        self.current_exp = ""
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=off_white_color, fg=label_color,
                               font=default_font, borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.current_exp = ""
        self.total_exp = ""
        self.update_label()
        self.update_total_label()

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=off_white_color, fg=label_color,
                           font=default_font, borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_exp = str(eval(f"{self.current_exp}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=off_white_color, fg=label_color,
                           font=default_font, borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_exp = str(eval(f"{self.current_exp}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=off_white_color, fg=label_color,
                           font=default_font, borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.total_exp += self.current_exp
        self.update_total_label()
        try:
            self.current_exp = str(eval(self.total_exp))
            self.total_exp = ""
        except Exception as e:
            self.current_exp = "Not Defined"
        finally:
            self.update_label()

    def create_equals_button(self):
            button = tk.Button(self.buttons_frame, text="=", bg=light_blue_color, fg=label_color,
                               font=default_font, borderwidth=0, command=self.evaluate)
            button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_exp
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_exp[:11])

    def bind_keys(self):
        self.root.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.root.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))
        for key in self.operations:
            self.root.bind(key, lambda event, operator=key: self.append_operator(operator))

    def run(self):
        self.root.mainloop()

calc = CustomCalculator()
calc.run()
