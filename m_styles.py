# m_styles.py
from tkinter import ttk

def set_custom_style():
    style = ttk.Style()
    style.theme_use('clam')

    # カスタムスタイルを作成 (エントリーボックス用)
    style.configure('Custom.TEntry', foreground='black', background='#f0f0f0', borderwidth=1)
    style.map('Custom.TEntry',
              fieldbackground=[('active', '#e0e0e0')],
              foreground=[('focus', 'black'), ('!focus', 'gray')])