from tkinter import ttk

# スタイルの定義
def main_style():
    style = ttk.Style()
    style.configure("TButton", foreground="black", background="white", font=("Helvetica", 12))
    style.configure("TLabel", foreground="blue", background="white", font=("Helvetica", 14))
    style.configure("TEntry", foreground="black", background="white", font=("Helvetica", 12))


