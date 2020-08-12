#! python3
# download youtube videos
#
# youtube -a [youtube url]
# a means also download audio file as mp3
#
# youtube [youtube url]
# download only video
#
# youtube [playlist url]
# download all videos from playlist

import codecs
import sys
from pathlib import Path

import youtube_dl
from moviepy.editor import *
from moviepy.video.io.VideoFileClip import VideoFileClip

# Examples for lib
# https://www.programcreek.com/python/example/98358/youtube_dl.YoutubeDL

MP3 = '.mp3'
EXT = 'ext'
PLAYLIST_TITLE = 'playlist_title'
CREATOR = 'creator'
TITLE = 'title'
PLAYLIST_INDEX = 'playlist_index'
ENTRIES = 'entries'
PLAYLIST = 'playlist'
TYPE = '_type'

# Compatibility fixes for Windows
if sys.platform == 'win32':
    # https://github.com/ytdl-org/youtube-dl/issues/820
    codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

home = str(Path.home())

# read an options and ur
argIndex = 1
alsoAudioFile = False

if str(sys.argv[1]).startswith('-a'):
    argIndex += 1
    alsoAudioFile = True

url_to_download = sys.argv[argIndex:]

# download video
# make it more sofisticated and configurable
dir = home + '\\Videos\\YoutubeDownload\\'
albumFolder = '%(creator)s - %(playlist_title)s\\'
outtmpl = dir + albumFolder +'%(autonumber)s-%(title)s.%(ext)s'
audioDir = dir + 'Audio\\'
retries = 3
cachedir = home + '\\Videos\\cacheYoutube\\'
verbose = None
format = 'mp4'
ydl_opts = {
    'forceformat': format,
    'format': format,
    'outtmpl': outtmpl,
    'retries': retries,
    'logtostderr': outtmpl == '-',
    'verbose': verbose,
    'cachedir': cachedir,
    'ignoreerrors': True,
}


def mp3(mp3_file_name, mp4_file):
    if alsoAudioFile:
        videofile = VideoFileClip(mp4_file)
        if not os.path.exists(audioDir):
            os.mkdir(audioDir)
        videofile.audio.write_audiofile(audioDir + mp3_file_name + MP3)


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    info = ydl.extract_info(url_to_download[0], download=True)
    if TYPE in info.keys() and info[TYPE] == PLAYLIST:
        for video in info[ENTRIES]:
            print('Video #%d: %s' % (video[PLAYLIST_INDEX], video[TITLE]))
            filename = f"{video[PLAYLIST_INDEX]:05d}-" + video[TITLE]

            #if creator is not present, then youtube dl use NA string
            creator = video[CREATOR]
            if creator is None: creator = 'NA'
            path_with_album = dir + creator + ' - ' + video[PLAYLIST_TITLE]

            mp4file = path_with_album + '\\' + filename + '.' + video[EXT]
            audioDir = path_with_album + ' - audio\\'
            mp3(filename, mp4file)
    else:
        mp3(info.get(TITLE), ydl.prepare_filename(info))


