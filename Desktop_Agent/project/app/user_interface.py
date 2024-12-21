import tkinter as tk
from tkinter import *
from tkinter import PhotoImage, ttk, messagebox
from .monitoring import Monitor
import threading
from pytz import all_timezones
from PIL import Image, ImageTk

class Employee_ActivityApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Activity Tracker")
        self.root.geometry("1450x400")  
        self.root.configure(bg="#00999c")
        self.root.resizable(False,False)

        # For adding the Agent Application ICON
        icon_ = Image.open("Desktop_Agent\\project\\app\\assets\\icon\\icon.png")
        icon_ = ImageTk.PhotoImage(icon_)
        self.root.iconphoto(True, icon_)

        
        self.monitor = None
        self.build_gui()

    def build_gui(self):
        # Apply a theme
        style = ttk.Style()
        style.theme_use('classic')

        # Configure Styles with Larger Font Sizes
        style.configure('TLabel', font=('Helvetica', 14), padding=5, background="#f0f0f0") 
        style.configure('TEntry', font=('Helvetica', 14), padding=5) 
        style.configure('TButton', font=('Helvetica', 14), padding=5, background="#4CAF50", foreground="black") 
        style.configure('TCheckbutton', font=('Helvetica', 14), padding=5, background="#ffffff") 
        style.configure('TCombobox', font=('Helvetica', 14 ),background="#ffffff")

        # Frame for Configuration
        config_frame = ttk.LabelFrame(self.root, text="Configuration", padding=(10, 10))
        config_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Screenshot Interval
        ttk.Label(config_frame, text="Screenshot Interval (minutes):").grid(row=0, column=0,pady=10, sticky="w",padx=10)
        self.interval_var = tk.IntVar(value=1)
        ttk.Entry(config_frame, textvariable=self.interval_var).grid(row=0, column=1, pady=10, padx=10) 

        # AWS S3 Bucket Name
        ttk.Label(config_frame, text="AWS S3 Bucket Name:").grid(row=0, column=2,pady=10, sticky="w",padx=10)
        self.s3_bucket_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.s3_bucket_var).grid(row=0, column=3, pady=10, padx=10)

        # AWS Access Key
        ttk.Label(config_frame, text="AWS Access Key:").grid(row=0, column=4,pady=10, sticky="w",padx=10)
        self.aws_access_key_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.aws_access_key_var).grid(row=0, column=5, pady=10, padx=10)

        # AWS Secret Key
        ttk.Label(config_frame, text="AWS Secret Key:").grid(row=2, column=0,pady=10, sticky="w",padx=10)
        self.aws_secret_key_var = tk.StringVar()
        ttk.Entry(config_frame, textvariable=self.aws_secret_key_var, show="*").grid(row=2, column=1, pady=10, padx=10)

        # AWS Region
        ttk.Label(config_frame, text="AWS Region:").grid(row=2, column=2,pady=10, sticky="w",padx=10)
        self.aws_region_var = tk.StringVar(value="ap-south-1")
        ttk.Entry(config_frame, textvariable=self.aws_region_var).grid(row=2, column=3, pady=10, padx=10)

        # Timezone
        ttk.Label(config_frame, text="Timezone:").grid(row=2, column=4,pady=10, sticky="w",padx=10)
        self.timezone_var = tk.StringVar(value="Asia/Kolkata")
        timezone_combobox = ttk.Combobox(config_frame, textvariable=self.timezone_var, values=all_timezones, state='readonly')
        timezone_combobox.grid(row=2, column=5, pady=10, padx=10)

        # Capture Screenshots
        self.capture_screenshots_var = tk.BooleanVar(value=True)
        ttk.Checkbutton(config_frame, text="Capture Screenshots", variable=self.capture_screenshots_var).grid(row=3, column=2, columnspan=2, pady=25, padx=10, sticky="w")

        # Buttons Frame
        button_frame = ttk.Frame(self.root,padding=(1,5))
        button_frame.pack(fill="x", padx=10, pady=10)

        # Start Tracking Button
        self.start_button = ttk.Button(button_frame, text="Start Tracking", command=self.start_monitoring)
        self.start_button.pack(side="left", expand=True, fill="x", padx=50)

        # Stop Tracking Button
        self.stop_button = ttk.Button(button_frame, text="Stop Tracking ", command=self.stop_monitoring, state="disabled")
        self.stop_button.pack(side="left", expand=True, fill="x", padx=250)

        # Clear Button
        self.clear_button = ttk.Button(button_frame, text="     Clear     ", command=self.clear_config)
        self.clear_button.pack(side="right", expand=True, fill="x", padx=50)
        

    def start_monitoring(self):
        config = {
            'interval': self.interval_var.get(),
            's3_bucket': self.s3_bucket_var.get(),
            'aws_access_key': self.aws_access_key_var.get(),
            'aws_secret_key': self.aws_secret_key_var.get(),
            'region_name': self.aws_region_var.get(),
            'timezone': self.timezone_var.get(),
            'capture_screenshots': self.capture_screenshots_var.get(),
        }

        # Validate Configuration
        if not all(config.values()):
            messagebox.showerror("Configuration Error", "Please fill in all configuration fields.")
            return

        self.monitor = Monitor(config)
        self.monitor.start_monitoring()
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        messagebox.showinfo("Tracking Started", "Employee_Activity tracking has started.")

    def stop_monitoring(self):
        if self.monitor:
            self.monitor.stop_monitoring()
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            messagebox.showinfo("Tracking Stopped", "Employee_Activity tracking has stopped.")
    
    def clear_config(self):
        #clear configuration using this....
        self.interval_var.set(5)
        self.s3_bucket_var.set("")
        self.aws_access_key_var.set("")
        self.aws_secret_key_var.set("")
        self.aws_region_var.set("ap-south-1")
        self.timezone_var.set("Asia/Kolkata")
        self.capture_screenshots_var.set(True)
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        if self.monitor:
            self.monitor.stop_monitoring()
            self.monitor = None
