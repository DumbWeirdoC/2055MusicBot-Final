from Tests.VDownloaderTests import musicDownloaderTest
from Tests.VSpotifyTests import musicSpotifyTest
from Tests.VDeezerTests import musicDeezerTest


tester = musicDownloaderTest()
tester.run()
tester = musicSpotifyTest()
tester.run()
tester = musicDeezerTest()
tester.run()
