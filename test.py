import os.path
import unittest
import datetime
import requests
from file_storage import write_to_csv, create_csv
from radio_scrapper import Radio_scapper

class Test_radio_scraper(unittest.TestCase):
    def setUp(self):
        self.scraper = Radio_scapper('http://listen.181fm.com/181-kickincountry_128k.mp3')

    def test_first_track(self):
        self.scraper.last_title = None
        self.scraper.last_time = None

        track = {
            'datetime': self.scraper.last_time or None,
            'title': 'Song',
            'duration': None
        }

        self.assertIsNone(track['duration'])
        self.assertEqual(track['title'], 'Song')

class TestFileStorage(unittest.TestCase):
    test_file = 'radio_tracks_test.csv'

    def setUp(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_track(self):
        create_csv(self.test_file)

        track = {"datetime": datetime.datetime(2025, 10, 8, 22, 0, 0),
                 'title': 'Song', 'duration': 100}
        write_to_csv(track, self.test_file)

        with open(self.test_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            self.assertEqual(len(lines), 2)
            self.assertIn('Song', lines[1])

if __name__ == '__main__':
    unittest.main()
