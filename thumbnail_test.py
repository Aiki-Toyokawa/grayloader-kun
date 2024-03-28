from pytube import YouTube
import requests
from pathlib import Path

# YouTubeの動画URL
video_url = 'https://www.youtube.com/watch?v=_O0h2WqEFjo'

# サムネイルを保存するフォルダのパス
save_folder = Path('.')

# YouTubeオブジェクトを作成
yt = YouTube(video_url)

# サムネイルのURLを取得
thumbnail_url = yt.thumbnail_url

# サムネイルの内容をダウンロード
response = requests.get(thumbnail_url)

# 応答が成功したか確認
if response.status_code == 200:
    # ファイル名に使用できない文字を除去するための関数
    def sanitize_filename(name):
        # ファイル名に使用できない文字をすべて削除
        forbidden_chars = '<>:"/\\|?*'
        for char in forbidden_chars:
            name = name.replace(char, '')
        # ファイル名が長すぎる場合は切り詰める
        return name[:150]  # Windowsのファイル名の最大長を考慮

    # サムネイルのファイル名（動画のタイトルに基づく）
    filename = sanitize_filename(yt.title) + '.jpg'

    # ファイルを保存するパスを指定
    file_path = save_folder / filename

    # 画像をファイルとして保存
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f'サムネイルを保存しました: {file_path}')
else:
    print('サムネイルのダウンロードに失敗しました')