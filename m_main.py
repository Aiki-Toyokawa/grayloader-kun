# m_main.py
import tkinter   as tk
import threading
import m_styles
from   tkinter   import ttk
from   m_modules import download_video_thread, display_resize_thumbnail

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("700x500")

#-----------------------------------#
# スタイル設定
m_styles.set_custom_style()

#-----------------------------------#



#-----------------------------------#
# UI

# URL入力欄
url_entry = ttk.Entry(root, width=80, style='Custom.TEntry')
url_entry.pack(pady=(10, 0))

# Canvasウィジェットを作成・描画 width=640, height=360
root.canvas = tk.Canvas(root, width=640, height=360, borderwidth=1, relief="solid")
root.canvas.pack(pady=(10, 0))

# ダウンロードボタン
download_button = ttk.Button(root, text="ダウンロード", command=lambda: threading.Thread(target=download_video_thread, args=(url_entry, label, display_resize_thumbnail, root)).start(), style='Custom.TButton')
download_button.pack(pady=(10, 0))

# 完了ラベル
label = tk.Label(root, text="")
label.pack()
#-----------------------------------#

root.mainloop()