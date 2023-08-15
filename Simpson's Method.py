
import tkinter as tk
from tkinter import messagebox

class MainApp:
    def __init__(self, root):
        self.root = root
        root.title("Simpsons Method")

        self.root.geometry("852x696")  # Adjusted window size

        self.title_label = tk.Label(root, text="Simpsons Method", font=("Helvetica", 20, "bold"))
        self.title_label.place(x=260, y=20, width=321, height=30)

        self.dd_label = tk.Label(root, text="Enter d:", font=("Helvetica", 14))
        self.dd_label.place(x=260, y=80, width=100, height=30)
        self.dd = tk.Entry(root, width=10)
        self.dd.place(x=400, y=80, width=150, height=30)

        self.yy_label = tk.Label(root, text="Enter y:", font=("Helvetica", 14))
        self.yy_label.place(x=260, y=140, width=100, height=30)
        self.yy = tk.Entry(root, width=10)
        self.yy.place(x=400, y=140, width=150, height=30)

        self.aa_label = tk.Label(root, text="Enter a:", font=("Helvetica", 14))
        self.aa_label.place(x=260, y=200, width=100, height=30)
        self.aa = tk.Entry(root, width=10)
        self.aa.place(x=400, y=200, width=150, height=30)

        self.bb_label = tk.Label(root, text="Enter b:", font=("Helvetica", 14))
        self.bb_label.place(x=260, y=260, width=100, height=30)
        self.bb = tk.Entry(root, width=10)
        self.bb.place(x=400, y=260, width=150, height=30)

        self.hh_label = tk.Label(root, text="Enter h:", font=("Helvetica", 14))
        self.hh_label.place(x=260, y=320, width=100, height=30)
        self.hh = tk.Entry(root, width=10)
        self.hh.place(x=400, y=320, width=150, height=30)

        self.result_label = tk.Label(root, text="Result:", font=("Helvetica", 14))
        self.result_label.place(x=260, y=380, width=100, height=30)
        self.reslt = tk.Entry(root, font=("Helvetica", 14))
        self.reslt.place(x=260, y=420, width=321, height=61)

        self.calculate_button = tk.Button(root, text="Calculate", font=("Helvetica", 14), command=self.calculate_result)
        self.calculate_button.place(x=350, y=510, width=131, height=41)

        self.reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=self.reset)
        self.reset_button.place(x=500, y=510, width=131, height=41)

        self.calculate_button.configure(bg="#FFA500", fg="white")
        self.reset_button.configure(bg="#FFA500", fg="white")
        root.configure(bg="#E0FFFF")

    def SimpsonsMethod(self, d, y, a, b, h):
        e = 2.7
        n = int((b - a) / h)
        lx = []
        ly = []

        def f(d, y, i):
            f = d / (y + e ** i)
            return f

        z = a
        for j in range(n + 1):
            lx.append(z)
            z = z + h

        for i in lx:
            p = f(d, y, i)
            ly.append(p)

        l = sum(ly[1:len(ly) - 1:2])
        ll = sum(ly[2:len(ly) - 1:2])
        integration = h / 3 * (ly[0] + 4 * ll + 2 * l + ly[len(ly) - 1])
        return integration
    

    def calculate_result(self):
        try:
            d1 = float(self.dd.get())
            y1 = float(self.yy.get())
            a1 = float(self.aa.get())
            b1 = float(self.bb.get())
            h1 = float(self.hh.get())
            y = self.SimpsonsMethod(d1, y1, a1, b1, h1)
            self.reslt.delete(0, tk.END)
            self.reslt.insert(0, str(y))
        except:
            self.show_errors_empty()

    def reset(self):
        self.dd.delete(0, tk.END)
        self.yy.delete(0, tk.END)
        self.aa.delete(0, tk.END)
        self.bb.delete(0, tk.END)
        self.hh.delete(0, tk.END)
        self.reslt.delete(0, tk.END)

    def show_errors_empty(self):
        messagebox.showerror("Errors", "Error fields are empty")

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()