import tkinter as tk
from tkinter import messagebox, ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class DataPlotterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Plotter Graphical User Interface")
        self.root.geometry("700x600")
        self.root.configure(bg="#f0f0f0")

        # Data storage
        self.x_data = []
        self.y_data = []
        self.plot_type = tk.StringVar(value="line")  # Default plot type

        # GUI Components
        self.create_widgets()

    def create_widgets(self):
        # Header Label
        header = tk.Label(self.root, text="Data Plotter Graphical User Interface", font=("Arial", 18, 'bold'), bg="#4a7a8c", fg="white")
        header.pack(fill="x", pady=(10, 20))

        # X and Y Entry Frame
        entry_frame = tk.Frame(self.root, bg="#f0f0f0")
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="X Value:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=0, padx=10)
        self.x_entry = tk.Entry(entry_frame, font=("Arial", 12), bd=2, relief='groove')
        self.x_entry.grid(row=0, column=1, padx=10)

        tk.Label(entry_frame, text="Y Value:", font=("Arial", 12), bg="#f0f0f0").grid(row=0, column=2, padx=10)
        self.y_entry = tk.Entry(entry_frame, font=("Arial", 12), bd=2, relief='groove')
        self.y_entry.grid(row=0, column=3, padx=10)

        # Buttons Frame
        button_frame = tk.Frame(self.root, bg="#f0f0f0")
        button_frame.pack(pady=10)

        button_style = {'font': ("Arial", 12, 'bold'), 'bg': "#4a7a8c", 'fg': "white", 'width': 15}
        tk.Button(button_frame, text="Add Data Point", command=self.add_data_point, **button_style).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Select Plot Type", command=self.select_plot_type, **button_style).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Plot Data", command=self.plot_data, **button_style).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Clear Data", command=self.clear_data, **button_style).grid(row=0, column=3, padx=5)

        # Figure for Plotting
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().pack(pady=20)

    def add_data_point(self):
        try:
            x_val = float(self.x_entry.get())
            y_val = float(self.y_entry.get())
            self.x_data.append(x_val)
            self.y_data.append(y_val)
            self.x_entry.delete(0, tk.END)
            self.y_entry.delete(0, tk.END)
            messagebox.showinfo("Success", "Data point added successfully!")
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for X and Y.")

    def select_plot_type(self):
        # Dialog box for selecting plot type
        dialog = tk.Toplevel(self.root)
        dialog.title("Select Plot Type")
        dialog.geometry("300x250")
        dialog.configure(bg="#e0e0e0")

        tk.Label(dialog, text="Choose Plot Type:", font=("Arial", 14, 'bold'), bg="#e0e0e0").pack(pady=20)

        # Radio buttons for plot type selection
        tk.Radiobutton(dialog, text="Line Plot", variable=self.plot_type, value="line", font=("Arial", 12), bg="#e0e0e0").pack(anchor="w", padx=20)
        tk.Radiobutton(dialog, text="Scatter Plot", variable=self.plot_type, value="scatter", font=("Arial", 12), bg="#e0e0e0").pack(anchor="w", padx=20)
        tk.Radiobutton(dialog, text="Area Plot", variable=self.plot_type, value="area", font=("Arial", 12), bg="#e0e0e0").pack(anchor="w", padx=20)

        # Close dialog button
        tk.Button(dialog, text="OK", command=dialog.destroy, font=("Arial", 12, 'bold'), bg="#4a7a8c", fg="white").pack(pady=20)

    def plot_data(self):
        self.ax.clear()
        if self.x_data and self.y_data:
            if self.plot_type.get() == "line":
                self.ax.plot(self.x_data, self.y_data, marker='o', color='b', label="Line Plot")
            elif self.plot_type.get() == "scatter":
                self.ax.scatter(self.x_data, self.y_data, color='r', label="Scatter Plot")
            elif self.plot_type.get() == "area":
                # For area plot, fill area between line plot and x-axis
                self.ax.fill_between(self.x_data, self.y_data, color='skyblue', alpha=0.4)
                self.ax.plot(self.x_data, self.y_data, marker='o', color='b', label="Area Plot")

            self.ax.set_title("Data Plot", fontweight='bold')
            self.ax.set_xlabel("X Values", fontweight='bold')
            self.ax.set_ylabel("Y Values", fontweight='bold')
            self.ax.legend()
            self.ax.grid(True, linestyle='--', alpha=0.7)
            self.canvas.draw()
        else:
            messagebox.showwarning("No data", "No data points to plot.")

    def clear_data(self):
        self.x_data.clear()
        self.y_data.clear()
        self.ax.clear()
        self.canvas.draw()
        messagebox.showinfo("Cleared", "Data points cleared.")

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = DataPlotterApp(root)
    root.mainloop()
