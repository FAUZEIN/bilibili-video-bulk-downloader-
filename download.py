import subprocess

def download_bilibili_videos(video_urls):
    for url in video_urls:
        command = f"you-get {url}"
        subprocess.run(command, shell=True)

if __name__ == "__main__":
    # Masukkan URL video Bilibili yang ingin diunduh ke dalam list berikut
    video_urls = [
        "https://www.bilibili.com/video/xxxxxx",
        "https://www.bilibili.com/video/yyyyyy",
        # Tambahkan URL lainnya sesuai kebutuhan
    ]

    download_bilibili_videos(video_urls)
