import tkinter as tk


class ModelApp:
    CORRECT_CODE = "50589"

    def __init__(self):
        self.code = ""

    def add_symbol(self, symbol):
        self.code += symbol

    def remove_last(self):
        self.code = self.code[:-1]

    def clear(self):
        self.code = ""

    def get_code(self):
        return self.code

    def check_code(self):
        return self.code == self.CORRECT_CODE


class ViewApp(tk.Frame):
    def __init__(self, master, callback):
        super().__init__(master)

        self.callback = callback

        frame_display = tk.Frame(self)
        frame_display.pack(fill="x")

        self.label = tk.Label(
            frame_display,
            bg="white",
            fg="black",               
            font=("Arial", 16, "bold"), 
            height=2
        )
        self.label.pack(fill="x")

        frames = []
        for _ in range(5):
            frame = tk.Frame(self)
            frame.pack(expand=True, fill="both")
            frames.append(frame)

        layout = [
            ("A", frames[0]), ("B", frames[0]), ("C", frames[0]), ("D", frames[0]),
            ("1", frames[1]), ("2", frames[1]), ("3", frames[1]),
            ("4", frames[2]), ("5", frames[2]), ("6", frames[2]),
            ("7", frames[3]), ("8", frames[3]), ("9", frames[3]),
            ("*", frames[4]), ("0", frames[4]), ("#", frames[4])
        ]

        for text, frame in layout:
            tk.Button(
                frame,
                text=text,
                command=lambda t=text: self.callback(t)
            ).pack(side="left", expand=True, fill="both")

    def refresh_label(self, text, success=False):
        if success:
            self.label.config(text="ACCESS GRANTED", bg="green")
        else:
            self.label.config(text=text, bg="white")


class ControllerApp:
    def __init__(self, root):
        self.model = ModelApp()
        self.view = ViewApp(root, self.press)
        self.view.pack(expand=True, fill="both")

    def press(self, symbol):

        if symbol == "*":                    
            self.model.remove_last()
            self.view.refresh_label(self.model.get_code())

        elif symbol == "#":                   
            if self.model.check_code():
                self.view.refresh_label("", success=True)
            else:
                self.view.refresh_label("WRONG PIN", success=False)
            self.model.clear()

        else:                                 
            self.model.add_symbol(symbol)
            self.view.refresh_label(self.model.get_code())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("PIN MVC App Variant - 5")
    app = ControllerApp(root)
    root.mainloop()