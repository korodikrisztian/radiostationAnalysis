from radio_scrapper import Radio_scapper
from file_storage import create_csv, write_to_csv

csv_file = 'radio_tracks.csv'
stream_url = 'http://listen.181fm.com/181-kickincountry_128k.mp3'

create_csv(csv_file)
scraper = Radio_scapper(stream_url)

def save_track(track):
    write_to_csv(track, csv_file)

scraper.run(callback=save_track)