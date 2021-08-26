import lastfmget
import unittest
import random

random.seed()

user = 'D3r3k523'

class Tests:
    @staticmethod
    def run(cfg_fn):
        lastfmget.init(cfg_fn)

        testcases = [ Tests.RawMethodTests, Tests.MethodTests ]
        
        for testcase in testcases:
            print(f'Running: {testcase.__name__}')
            suite = unittest.defaultTestLoader.loadTestsFromTestCase(testcase)
            unittest.TextTestRunner().run(suite)

    class RawMethodTests(unittest.TestCase):
        def test_user_info_basic(self):
            userinfo = lastfmget.user_info_raw(user)
            self.assertEqual(userinfo['user']['name'], user)

        def test_user_recent_tracks_basic(self):
            recenttracks = lastfmget.user_recent_tracks_raw(user)
            self.assertEqual(recenttracks['recenttracks']['@attr']['user'], user)

        def test_user_top_artists_basic(self):
            topartists = lastfmget.user_top_artists_raw(user)
            self.assertEqual(topartists['topartists']['@attr']['user'], user)

        def test_user_top_albums_basic(self):
            topalbums = lastfmget.user_top_albums_raw(user)
            self.assertEqual(topalbums['topalbums']['@attr']['user'], user)

        def test_user_top_tracks_basic(self):
            toptracks = lastfmget.user_top_tracks_raw(user)
            self.assertEqual(toptracks['toptracks']['@attr']['user'], user)

        def test_user_weekly_chart_list_basic(self):
            chartlist = lastfmget.user_weekly_chart_list_raw(user)
            self.assertEqual(chartlist['weeklychartlist']['@attr']['user'], user)

        def test_user_weekly_artist_chart_basic(self):
            artistchart = lastfmget.user_weekly_artist_chart_raw(user)
            self.assertEqual(artistchart['weeklyartistchart']['@attr']['user'], user)

        def test_user_weekly_album_chart_basic(self):
            albumchart = lastfmget.user_weekly_album_chart_raw(user)
            self.assertEqual(albumchart['weeklyalbumchart']['@attr']['user'], user)

        def test_user_weekly_track_chart_basic(self):
            trackchart = lastfmget.user_weekly_track_chart_raw(user)
            self.assertEqual(trackchart['weeklytrackchart']['@attr']['user'], user)

        def test_user_recent_tracks_count(self):
            countvals = [ 0, 50, 200, 300 ] + random.choices(range(0, 501), k=6)
            for count in countvals:
                recenttracks = lastfmget.user_recent_tracks(user, count=count)
                self.assertEqual(len(recenttracks), count)

    class MethodTests(unittest.TestCase):
        def test_user_info_compare_to_raw(self):
            userinforaw = lastfmget.user_info_raw(user)
            userinfo    = lastfmget.user_info(user)
            self.assertEqual(userinfo['name'], userinforaw['user']['name'])

        # def test_user_recent_tracks_basic(self):
        #     recenttracksraw = lastfmget.user_recent_tracks_raw(user)
        #     recenttracks    = lastfmget.user_recent_tracks(user)
        #     self.assertEqual(recenttracks['recenttracks']['@attr']['user'], user)

        # def test_user_top_artists_basic(self):
        #     topartists = lastfmget.user_top_artists(user)
        #     self.assertEqual(topartists['topartists']['@attr']['user'], user)

        # def test_user_top_albums_basic(self):
        #     topalbums = lastfmget.user_top_albums(user)
        #     self.assertEqual(topalbums['topalbums']['@attr']['user'], user)

        # def test_user_top_tracks_basic(self):
        #     toptracks = lastfmget.user_top_tracks(user)
        #     self.assertEqual(toptracks['toptracks']['@attr']['user'], user)

        # def test_user_weekly_chart_list_basic(self):
        #     chartlist = lastfmget.user_weekly_chart_list(user)
        #     self.assertEqual(chartlist['weeklychartlist']['@attr']['user'], user)

        # def test_user_weekly_artist_chart_basic(self):
        #     artistchart = lastfmget.user_weekly_artist_chart(user)
        #     self.assertEqual(artistchart['weeklyartistchart']['@attr']['user'], user)

        # def test_user_weekly_album_chart_basic(self):
        #     albumchart = lastfmget.user_weekly_album_chart(user)
        #     self.assertEqual(albumchart['weeklyalbumchart']['@attr']['user'], user)

        # def test_user_weekly_track_chart_basic(self):
        #     trackchart = lastfmget.user_weekly_track_chart(user)
        #     self.assertEqual(trackchart['weeklytrackchart']['@attr']['user'], user)
