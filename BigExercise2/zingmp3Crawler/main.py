from zingmp3 import Base
import os 

def downloadMusic(url):
    name = url.split('/')[-1].replace('-', ' ')
    root = os.path.join(os.getcwd(), 'Music')
    if not os.path.exists(root):
        os.mkdir(root)
    path = os.path.join(root, name)
    Base(
        url=url,
        path_save=path,
        show_json_info=False,
        down_lyric=False,
        is_login=False,
    )
