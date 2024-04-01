# m_modules.py
import requests
from tkinter import messagebox
from io      import BytesIO
from PIL     import Image, ImageTk
from pytube  import YouTube

#----------------------------------------------------------------------#
# 動画ダウンロード関数
def download_video_thread(url_entry, label, root):
    url = url_entry.get()
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="downloads")
        root.after(0, label.config, {"text": "ダウンロード完了"})
        
        #-------------------------------#
        # サムネイルのダウンロード
        thumbnail_url = yt.thumbnail_url
        response = requests.get(thumbnail_url)

        # サムネイル画像の保存名（動画IDを使用）
        thumbnail_filename = 'thumbs/' + yt.video_id + '.jpg'
        with open(thumbnail_filename, 'wb') as f:
            f.write(response.content)
        #-------------------------------#
        
        # サムネイル表示関数呼び出し
        root.after(0, display_resize_thumbnail, yt.thumbnail_url, root)

    # エラー処理
    except Exception as e:
        root.after(0, label.config, {"text": f"エラー : URLの動画が見つかりませんでした。URL間違ってるYO"})
        root.after(0, lambda: messagebox.showerror("エラー", f"動画のダウンロードに失敗しました: {e}"))
#----------------------------------------------------------------------#


#----------------------------------------------------------------------#
# サムネリサイズ＆表示関数
def display_resize_thumbnail(url, root):
    response = requests.get(url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)

    # Canvasのサイズ
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
    canvas = root.canvas  # 'root.canvas' は 'main.py' で定義された canvas ウィジェットを指す
    canvas.image = photo  # これにより、画像がガベージコレクションによって消去されるのを防ぎます

    # リサイズされた画像をCanvasの中央に配置
    x_position = (canvas_width - new_width) / 2
    y_position = (canvas_height - new_height) / 2
    canvas.create_image(x_position + new_width / 2, y_position + new_height / 2, anchor='center', image=photo)
#----------------------------------------------------------------------#