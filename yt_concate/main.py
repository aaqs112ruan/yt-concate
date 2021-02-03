# get video list from youtube channel
import urllib.request
import json
from yt_concate.settings import API_KEY
CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


def get_all_video_in_channel(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    # 使用API的網址的基底
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
    # 補上需要跟API要甚麼東西 成為一個完整的網址 內有此頻道所有的影片之資訊內容
    first_url = base_search_url + f'key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)
        # 得到每個影片的網址並加入清單
        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
