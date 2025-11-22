import time
import requests
from datetime import datetime

class Radio_scapper:
    def __init__(self, stream_url):
        self.stream_url = stream_url
        self.last_time = None
        self.last_title = None

    def get_metadata(self):
        try:
            headers = {'Icy-MetaData': '1', 'User-Agent': 'Mozilla/5.0'}
            response = requests.get(self.stream_url, headers=headers, stream=True, timeout=10)
            metaint = int(response.headers.get('icy-metaint', 0))

            if metaint:
                stream = response.raw
                stream.read(metaint)
                meta_length = ord(stream.read(1)) * 16
                metadata = stream.read(meta_length).decode('utf-8', errors='ignore')

                if 'StreamTitle=' in metadata:
                    raw_title = metadata.split("StreamTitle='")[1].split("';")[0].strip()
                    now = datetime.now()#.strftime("%Y-%m-%d %H:%M:%S")

                    if raw_title != self.last_title and raw_title:
                        track = {
                            'datetime': now,
                            'title': raw_title,
                        }

                        self.last_title = raw_title

                        return track
        except requests.RequestException as e:
            time.sleep(10)

        return None

    def run(self, callback=None):
        while True:
            track = self.get_metadata()
            if track and callback:
                callback(track)