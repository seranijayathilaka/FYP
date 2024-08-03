import pandas as pd
import numpy as np
import time
import tkinter as tk
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
from keras.models import load_model
import threading
import datetime
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("DL Based Cyber Attack Detection on Power Grids")
        self.geometry("800x600")
        self.configure(background='#1e3c72')

        style = ttk.Style(self)
        style.configure('Custom.TButton', font=('Arial', 14), relief="raised")
        style.configure('Custom.TNotebook.Tab', font=('Arial', 14))

        self.notebook = ttk.Notebook(self, style='Custom.TNotebook')
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)

        self.create_tabs()
        self.prediction_running = False
        self.prediction_thread = None

    def create_tabs(self):
        home_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        process_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        info_tab = ttk.Frame(self.notebook, style='Custom.TFrame')
        team_tab = ttk.Frame(self.notebook, style='Custom.TFrame')

        self.notebook.add(home_tab, text="Home")
        self.notebook.add(process_tab, text="Process")
        self.notebook.add(info_tab, text="Info")
        self.notebook.add(team_tab, text="Our Team")

        self.add_process_content(process_tab)
        self.add_home_content(home_tab)
        self.add_info_content(info_tab)
        self.add_team_content(team_tab)

    def add_home_content(self, tab):
        image = Image.open(r"F:\fyp\GUI\background_image.jpg")  # Add background image to the home page
        image = image.convert("RGB")
        bg_image = ImageTk.PhotoImage(image)
        bg_label = tk.Label(tab, image=bg_image)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        bg_label.image = bg_image

        # Project overview
        user_info1 = """
        DEEP LEARNING - BASED CYBER ATTACK DETECTION  \n IN POWER GRIDS WITH INCREASING  \n RENEWABLE ENERGY PENETRATION"""
        user_info2 = """- The increasing integration of renewable energy sources like solar and wind into power \n grids introduces new cybersecurity challenges. \n -The intermittent nature of these energy sources and the complexity of managing their\n variability create potential vulnerabilities that malicious actors could exploit through \n cyber attacks. \n -This project aims to develop a robust and intelligent system for detecting such cyber \n attacks in power grids  with high levels of renewable energy penetration.
        """
        user_label1 = tk.Label(tab, text=user_info1, background='white', foreground='#1e3c72', font=("Tahoma", 28), justify="center")
        user_label1.pack(padx=20, pady=20)

        user_label2 = tk.Label(tab, text=user_info2, background='white', foreground='black', font=("Tahoma", 18), justify="left")
        user_label2.pack(padx=20, pady=20)

        user_label1.lift()
        user_label2.lift()

        continue_button = ttk.Button(tab, text="Click to Continue", command=lambda: self.notebook.select(1), style='Custom.TButton')
        continue_button.config(style='Custom.TButton')
        continue_button.pack(pady=20)

    def add_info_content(self, tab):
        # Title
        title_label = tk.Label(tab, text="Deep Learning-based Cyber Attack Detection on Power Grids", background='#1e3c72', foreground='white', font=("Tahoma", 28), justify="center")
        title_label.pack(padx=20, pady=20)

        info_text = """
        Project Overview:\n
        The project aims to develop a real-time cyber attack detection system for power grids using deep learning techniques.It utilizes neural networks to analyze incoming data streams for anomaly detection.\n\n
        Key Features:\n
        - Real-time data loading from external power systems.\n
        - DL model (Transformer model) for predicting cyber attacks.\n
        - Prediction results displayed.\n\n
        Technologies Used:\n
        - Python\n
        - TensorFlow/Keras for DL model development\n
        - GUI framework (Tkinter)\n
        - Data/Excel handling (pandas library, numpy)\n\n
        Data Sources: The system processes real-time data streams sourced from created PSCAD model based on CEB data.\n\n
        Creation Date: 12/05/2024               Last Update Date: 12/07/2024\n\n
        Contact Information: For inquiries or collaboration opportunities, please contact fypgroup7@gmail.com.\n\n"""

        info_label = tk.Label(tab, text=info_text, background='white', foreground='black', font=("Tahoma", 12), justify="left")
        info_label.pack(padx=20, pady=(0, 20), fill="both", expand=True)

    def add_team_content(self, tab):
        title_label = tk.Label(tab, text="Our Team", background='#1e3c72', foreground='white', font=("Arial", 24, "bold"))
        title_label.grid(row=0, column=0, columnspan=5, pady=(20, 10))

        background_label = tk.Label(tab, bg='#1e3c72')
        background_label.grid(row=1, column=0, rowspan=2, columnspan=5, sticky="nsew")

        # Team info
        member_info = [
            {"name": "V.Logeeshan", "position": "Supervisor", "info": "logeeshanv@uom.lk"},
            {"name": "S.kumarawadu", "position": "Co-Supervisor", "info": "  sisil@uom.lk  "},
            {"name": "M.A.S.P.Dayarathna", "position": "Team member", "info": "sasikadayarathna708@gmail.com"},
            {"name": "M.S.M.Jayathilaka", "position": "Team member", "info": "    seranij15@gmail.com    "},
            {"name": "R.M.V.A. Bandara", "position": "Team member", "info": "venuraavishka1@gmail.com"}
        ]

        image_paths = [
            "F:/fyp/GUI/m4.jpg",
            "F:/fyp/GUI/m5.jpg",
            "F:/fyp/GUI/m1.jpg",
            "F:/fyp/GUI/m2.jpg",
            "F:/fyp/GUI/m3.jpg"
        ]

        # Resize images
        max_image_size = (200, 200)
        photo_images = []
        for path in image_paths:
            image = Image.open(path).convert("RGB")
            image = image.resize(max_image_size)
            photo = ImageTk.PhotoImage(image)
            photo_images.append(photo)

        # Grid layout configuration
        for i in range(2):
            tab.grid_rowconfigure(i + 1, weight=1, minsize=200)  # Minimum height for each row
        for j in range(5):
            tab.grid_columnconfigure(j, weight=1, minsize=200)  # Minimum width for each column

        # Display
        for idx, (photo, info) in enumerate(zip(photo_images, member_info)):
            # Determine grid row and column based on the index
            if idx < 2:  # First row, 2nd and 4th columns
                row = 1
                col = 2 * idx + 1
            else:  # Second row, 1st, 3rd, and 5th columns
                row = 2
                col = (idx - 2) * 2

            # Create a frame
            member_frame = tk.Frame(tab, bg='#1e3c72')
            member_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

            if info:
                member_label = tk.Label(member_frame, image=photo, bg='#1e3c72')
                member_label.image = photo
                member_label.pack()

                member_info_label = tk.Label(member_frame, text=f"{info['name']}\n{info['position']}\n{info['info']}",
                                             bg='#1e3c72', fg='white', font=("Arial", 14), justify="center")
                member_info_label.pack()

        # Adjust column weights for even distribution
        for j in range(5):
            tab.grid_columnconfigure(j, weight=1)

    def add_process_content(self, tab):
        file_label = ttk.Label(tab, text="", background='#1e3c72', foreground='white', font=("Arial", 12))
        file_label.pack(pady=(10, 5))

        load_button = ttk.Button(tab, text="Feed Data", command=lambda: self.load_excel(file_label), style='Custom.TButton')
        load_button.pack(pady=5)

        self.predict_button = ttk.Button(tab, text="Start Prediction", command=self.start_prediction_thread, state=tk.DISABLED, style='Custom.TButton')
        self.predict_button.pack(pady=5)

        self.stop_button = ttk.Button(tab, text="Stop Prediction", command=self.stop_prediction, state=tk.DISABLED, style='Custom.TButton')
        self.stop_button.pack(pady=5)

        self.data_frame = ttk.Frame(tab, style='Custom.TFrame')
        self.data_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.tree = ttk.Treeview(self.data_frame, columns=(1, 2, 3, 4), show="headings", height=10)
        self.tree.pack(side="left", fill="both", expand=True)

        self.tree.heading(1, text="Column 1")
        self.tree.heading(2, text="Column 2")
        self.tree.heading(3, text="Column 3")
        self.tree.heading(4, text="Column 4")

        self.tree.column(1, width=150)
        self.tree.column(2, width=150)
        self.tree.column(3, width=150)
        self.tree.column(4, width=150)

        y_scrollbar = ttk.Scrollbar(self.data_frame, orient="vertical", command=self.tree.yview)
        y_scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=y_scrollbar.set)

        self.result_label = ttk.Label(tab, text="", background='white', foreground='black', font=("Arial", 16, "bold"))
        self.result_label.pack(pady=5)

        self.figures = []
        self.axes = []
        self.canvases = []

        self.plot_frame = ttk.Frame(tab, style='Custom.TFrame')
        self.plot_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.plot_canvas = tk.Canvas(self.plot_frame, background='white')
        self.plot_scrollbar = ttk.Scrollbar(self.plot_frame, orient="vertical", command=self.plot_canvas.yview)
        self.plot_scrollbar.pack(side="right", fill="y")
        self.plot_canvas.configure(yscrollcommand=self.plot_scrollbar.set)
        self.plot_canvas.pack(fill="both", expand=True, side="left")

        self.scrollable_frame = ttk.Frame(self.plot_canvas, style='Custom.TFrame')
        self.scrollable_frame.bind("<Configure>", lambda e: self.plot_canvas.configure(scrollregion=self.plot_canvas.bbox("all")))

        self.plot_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        # Initialize with empty plots
        self.sheet_names = []  # list to store sheet names
        for i in range(5):  # 5 sheets
            figure = Figure(figsize=(10, 2), dpi=100)
            ax = figure.add_subplot(111)
            self.figures.append(figure)
            self.axes.append(ax)

            canvas = FigureCanvasTkAgg(figure, master=self.scrollable_frame)
            canvas.get_tk_widget().pack(padx=10, pady=10, fill='both', expand=True)
            self.canvases.append(canvas)

        # Bind window resize event
        self.bind('<Configure>', self.resize_plots)

    def resize_plots(self, event):
        for canvas in self.canvases:
            canvas.get_tk_widget().config(width=self.plot_frame.winfo_width())

    def load_excel(self, file_label):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            file_label.config(text=f"Loaded File: {file_path}")
            self.file_path = file_path
            self.data_sequence = self.load_and_preprocess_data(file_path)
            self.populate_treeview()

    def load_and_preprocess_data(self, file_path):
        all_data = []
        self.column_headers = []
        xls = pd.ExcelFile(file_path)
        self.sheet_data = []
        self.sheet_names = xls.sheet_names  # Store sheet names
        for sheet_name in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name)
            self.column_headers.extend(df.columns[:4])
            self.sheet_data.append(df.iloc[:, :4])
            all_data.append(df.iloc[:, :4].values)

        data_sequence = np.concatenate(all_data, axis=1)
        return data_sequence

    def populate_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for idx, header in enumerate(self.column_headers[:4]):
            self.tree.heading(f"#{idx+1}", text=header)
            self.tree.column(f"#{idx+1}", anchor=tk.CENTER)

        for row in self.data_sequence:
            row = [str(item).strip('[]') for item in row]
            self.tree.insert("", "end", values=row)

        self.predict_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)

        # Update plot titles with sheet names
        for i, sheet_name in enumerate(self.sheet_names):
            self.axes[i].set_title(sheet_name)
            self.canvases[i].draw()

    def start_prediction_thread(self):
        self.prediction_running = True
        self.prediction_thread = threading.Thread(target=self.predict_and_display)
        self.prediction_thread.start()

    def stop_prediction(self):
        self.prediction_running = False
        self.predict_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def predict_and_display(self):
        self.model = load_model('F:/fyp/GUI/model.h5')
        num_rows = len(self.data_sequence)
        window_size = 30
        step_size = 30

        for start_idx in range(0, num_rows - window_size + 1, step_size):
            if not self.prediction_running:
                break

            window_data = self.data_sequence[start_idx:start_idx + window_size]

            if window_data.shape == (window_size, 20):
                reshaped_data = window_data.reshape((30, 20, 1))
                reshaped_data = np.expand_dims(reshaped_data, axis=0)

                prediction = self.model.predict(reshaped_data)
                attack_detected = "Attack Detected" if prediction[0][0] > 0.5 else "No Attack"

                self.update_data_display(window_data, attack_detected)
                self.update_graphs(start_idx, window_size)

                if attack_detected == "Attack Detected":
                    self.result_label.config(text=attack_detected, foreground='red')
                else:
                    self.result_label.config(text=attack_detected, foreground='green')

                self.update()
                time.sleep(30)

        self.predict_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_data_display(self, window_data, attack_detected):
        self.tree.after(0, self._update_data_display, window_data, attack_detected)

    def _update_data_display(self, window_data, attack_detected):
        for item in self.tree.get_children():
            self.tree.delete(item)

        for row in window_data:
            row = [str(item).strip('[]') for item in row]
            self.tree.insert("", "end", values=row)

        last_item = self.tree.get_children()[-1]
        if attack_detected == "Attack Detected":
            self.tree.tag_configure('red_tag', background='red')
            self.tree.item(last_item, tags=('red_tag',))
        else:
            self.tree.tag_configure('green_tag', background='green')
            self.tree.item(last_item, tags=('green_tag',))

    def update_graphs(self, start_idx, window_size):
        for i, (df, sheet_name) in enumerate(zip(self.sheet_data, self.sheet_names)):
            self.axes[i].clear()
            self.axes[i].set_title(sheet_name)
            self.axes[i].set_xlabel('Time')
            self.axes[i].set_ylabel('Values')
            for col in df.columns:
                # Plot data up to the current window
                self.axes[i].plot(df.index[:start_idx + window_size], df[col][:start_idx + window_size], label=col)

            self.axes[i].legend()
            self.canvases[i].draw()

# Create and run the GUI
if __name__ == "__main__":
    gui = GUI()
    gui.mainloop()
