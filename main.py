# mian.py
import tkinter as tk
from pytube import YouTube
from tkinter import messagebox
from PIL import Image, ImageTk
import requests
from io import BytesIO

root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("700x500")  # ウィンドウサイズを設定

def download_video():
    url = url_entry.get()
    yt = YouTube(url)
    try:
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="downloads")
        label.config(text="ダウンロード完了")

        #-------------------------------
        # サムネイルのダウンロード
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)

        # サムネイル画像のファイル名（動画IDを使用）
        thumbnail_filename = 'thumbs/' + yt.video_id + '.jpg'
        with open(thumbnail_filename, 'wb') as f:
            f.write(response.content)
        #------------------------------
        display_thumbnail(yt.thumbnail_url)
    except Exception as e:
        label.config(text=f"エラー:{e}")
        messagebox.showerror("エラー", f"動画のダウンロードに失敗しました: {e}")

#-----------サムネイルリサイズ関数-----------#
def display_thumbnail(url):
    # 画像のダウンロード
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)

    canvas_width  = 640
    canvas_height = 360

    # 画像のオリジナルサイズ
    original_width, original_height = img.size

    # 画像の縦横比を保持しつつ、Canvasのサイズに合わせて調整
    ratio = min(canvas_width / original_width, canvas_height / original_height)
    new_width = int(original_width * ratio)
    new_height = int(original_height * ratio)

    # リサイズされた画像を作成
    img_resized = img.resize((new_width, new_height), Image.LANCZOS)
    photo = ImageTk.PhotoImage(img_resized)

    # イメージオブジェクトをCanvasの参照として保持
    canvas.image = photo

    # リサイズされた画像をCanvasの中央に配置
    x_position = (canvas_width - new_width) / 2
    y_position = (canvas_height - new_height) / 2
    canvas.create_image(x_position, y_position, anchor='nw', image=photo)
#-----------サムネイルリサイズ関数-----------#

#-----------UI-----------#

# URL入力欄
url_entry = tk.Entry(root, width=80)
url_entry.pack(pady=(10, 0))

# Canvasウィジェットを作成・描画 width=640, height=360
canvas = tk.Canvas(root, width=640, height=360, borderwidth=0, relief="solid")
canvas.pack(pady=(10, 0))

# ダウンロードボタン
download_button = tk.Button(root, text="ダウンロード", command=download_video)
download_button.pack(pady=(10, 0))

# 完了ラベル
label = tk.Label(root, text="")
label.pack()

#-----------UI-----------#

root.mainloop()
