import os
from yt_dlp import YoutubeDL

links = os.environ.get("LINKS", "").split()
max_videos = int(os.environ.get("MAX_VIDEOS", "300"))

if not links:
    raise SystemExit("Нет ссылок. Вставь их в поле links при запуске.")

os.makedirs("memes", exist_ok=True)

opts = {
    "outtmpl": "memes/%(autonumber)s_%(id)s.%(ext)s",
    "format": "mp4/best",
    "playlistend": 300,          # максимум с одной ссылки
    "max_downloads": max_videos,  # общий максимум
    "ignoreerrors": True,
    "quiet": True,
}

try:
    with YoutubeDL(opts) as ydl:
        ydl.download(links)
except Exception as e:
    print("Остановился:", e)

print("Скачано роликов:", len(os.listdir("memes")))
