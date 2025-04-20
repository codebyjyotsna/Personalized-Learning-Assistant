from youtube_dl import YoutubeDL

def get_video_metadata(video_url):
    ydl_opts = {"quiet": True}
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(video_url, download=False)
        return {
            "title": info_dict.get("title"),
            "duration": info_dict.get("duration"),
            "description": info_dict.get("description")
        }
