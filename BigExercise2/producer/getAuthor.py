# import os
# import requests

# # url = 'https://api-v2.soundcloud.com/search/tracks?q=justin bieber&sc_a_id=831a4926-c3e1-4aa5-89fc-146fa27d2874&variant_ids=&facet=genre&user_id=35779-276519-26572-748988&client_id=PANENeeumEFxeUKuTj575zguSBQI5DwE&limit=20&offset=0&linked_partitioning=1&app_version=1587041896&app_locale=en'
# url = "https://zingmp3.vn/api/artist/get-list?id=IWZ9Z08O&type=genre&sort=listen&start={}&count={}&ctime=1587316884&sig=d01cf45e8e33970a118fa417e43ee6af485099ae6dbce6629d786704c3d2719f7af11c6c1438dff8b2a8e6d8029c468b6de4a03a907e1f267e16ff9e32a33818&api_key=38e8643fb0dc04e8d65b99994d3dafff"
# for i in range(4):
#     resp = requests.get(url.format(150*i, 150))
#     data = resp.json()
#     authors = data['data']['items']
#     file_author = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'playlist.txt')
#     with open(file_author, 'a') as f:
#         for x in authors:
#             host = 'https://soundcloud.com/search?q='    
#             f.write(host + x['name']+'\n')


import random
import os
file_out = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'list.txt')
file_author = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'playlist.txt')
with open(file_author, 'r') as f:
    lines = f.readlines()
    random.shuffle(lines)
    with open(file_out, 'w') as f2:
        for line in lines:
            f2.write(line)