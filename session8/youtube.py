from __future__ import unicode_literals
import youtube_dl

ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
   r = ydl.extract_info('https://www.youtube.com/watch?v=82D9N6ah2tg')
   print(r)
info = []
info.append(r)
# from __future__ import unicode_literals
# import youtube_dl


# class MyLogger(object):
#     def debug(self, msg):
#         pass

#     def warning(self, msg):
#         pass

#     def error(self, msg):
#         print(msg)


# def my_hook(d):
#     if d['status'] == 'finished':
#         print('Done downloading, now converting ...')


# ydl_opts = {
#     'format': 'bestaudio/best',
#     'postprocessors': [{
#         'key': 'FFmpegExtractAudio',
#         'preferredcodec': 'mp3',
#         'preferredquality': '192',
#     }],
#     'logger': MyLogger(),
#     'progress_hooks': [my_hook],
# }
# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download(['https://www.youtube.com/watch?v=BaW_jenozKc'])