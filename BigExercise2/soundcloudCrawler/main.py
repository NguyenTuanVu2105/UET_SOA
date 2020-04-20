import soundcloud
import os
import requests

def downloadMusic(url, path):
    try:
        soundcloud.Base(
            url=url,
            file_save=path,
            show_json_info=False,
            down_lyric=False,
            is_login=False,
        )
    except Exception as e:
        root = os.path.join(path, 'ERROR')
        if not os.path.exists(root):
            os.mkdir(root)
        path = os.path.join(root, 'errors.txt')
        with open(path, 'a') as f:
            f.write(url)
        print("Error", url)


def downloadPlaylist(url):
    search = 'https://api-v2.soundcloud.com/search/tracks?q={}&sc_a_id=831a4926-c3e1-4aa5-89fc-146fa27d2874&variant_ids=&facet=genre&user_id=66845-590873-55896-469501&client_id=VcpZHwGsLAniJbVr2N3apnGIyJsEZGKb&limit={}&offset=0&linked_partitioning=1&app_version=1587399492&app_locale=en'
    if 'search?q=' in url:
        name = url.split('=')[-1]
        print("Searching for", name, '........')
        resp = requests.get(search.format(name, 50))
        res = resp.json()['collection']
        for music in res:
            root = os.path.join(os.getcwd(), 'Music')
            if not os.path.exists(root):
                os.mkdir(root)
            path = os.path.join(root, name.replace('%20', ' '))
            downloadMusic(music['permalink_url'], path)
    else:
        props = url.split('/')
        if 'set' in props[-1]:
            name = props[-2] 
        else:
            name = props[-1]
        root = os.path.join(os.getcwd(), 'Music')
        if not os.path.exists(root):
            os.mkdir(root)
        path = os.path.join(root, name)
        downloadMusic(url, path)


# downloadMusic('https://soundcloud.com/daddy-yankee-official/con-calma-feat-snow', os.getcwd())
# downloadPlaylist('https://soundcloud.com/search?q=le%20bao%20binh')