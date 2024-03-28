# main.py
import tkinter as tk
from m_modules import download_video_thread, display_resize_thumbnail
import threading

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("700x500")

#-----------------------------------#
# UI

# URL入力欄
url_entry = tk.Entry(root, width=80)
url_entry.pack(pady=(10, 0))

# Canvasウィジェットを作成・描画 width=640, height=360
root.canvas = tk.Canvas(root, width=640, height=360, borderwidth=0, relief="solid")
root.canvas.pack(pady=(10, 0))

# ダウンロードボタン
download_button = tk.Button(root, text="ダウンロード", command=lambda: threading.Thread(target=download_video_thread, args=(url_entry, label, display_resize_thumbnail, root)).start())
download_button.pack(pady=(10, 0))

# 完了ラベル
label = tk.Label(root, text="")
label.pack()
#-----------------------------------#

root.mainloop()