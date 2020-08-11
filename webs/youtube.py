#! python3
# download youtube video
#
# youtube -a [youtube url]
# a means also download audio file as mp3
#
# youtube [youtube url]
# download only video

from pathlib import Path

import youtube_dl

import codecs
import sys
import os
from moviepy.editor import *

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

#download video
#make it more sofisticated and configurable
outtmpl = home + '\\Videos\\YoutubeDownload\\%(title)s.%(ext)s'
audioDir = home + '\\Videos\\YoutubeDownload\\Audio\\'
retries = 3
cachedir = home + '\\Videos\\cacheYoutube\\'
verbose = None
format = 'mp4'
ydl_opts = {
    # 'usenetrc': opts.usenetrc,
    # 'username': opts.username,
    # 'password': opts.password,
    # 'twofactor': opts.twofactor,
    # 'videopassword': opts.videopassword,
    # 'ap_mso': opts.ap_mso,
    # 'ap_username': opts.ap_username,
    # 'ap_password': opts.ap_password,
    # 'quiet': (opts.quiet or any_getting or any_printing),
    # 'no_warnings': opts.no_warnings,
    # 'forceurl': opts.geturl,
    # 'forcetitle': opts.gettitle,
    # 'forceid': opts.getid,
    # 'forcethumbnail': opts.getthumbnail,
    # 'forcedescription': opts.getdescription,
    # 'forceduration': opts.getduration,
    # 'forcefilename': opts.getfilename,
    'forceformat': format,
    # 'forcejson': opts.dumpjson or opts.print_json,
    # 'dump_single_json': opts.dump_single_json,
    'format': format,
    # 'listformats': opts.listformats,
    'outtmpl': outtmpl,
    # 'autonumber_size': opts.autonumber_size,
    # 'autonumber_start': opts.autonumber_start,
    # 'restrictfilenames': opts.restrictfilenames,
    # 'ignoreerrors': opts.ignoreerrors,
    # 'force_generic_extractor': opts.force_generic_extractor,
    # 'ratelimit': opts.ratelimit,
    # 'nooverwrites': opts.nooverwrites,
    'retries': retries,
    # 'fragment_retries': opts.fragment_retries,
    # 'skip_unavailable_fragments': opts.skip_unavailable_fragments,
    # 'keep_fragments': opts.keep_fragments,
    # 'buffersize': opts.buffersize,
    # 'noresizebuffer': opts.noresizebuffer,
    # 'http_chunk_size': opts.http_chunk_size,
    # 'continuedl': opts.continue_dl,
    # 'noprogress': opts.noprogress,
    # 'playliststart': opts.playliststart,
    # 'playlistend': opts.playlistend,
    # 'playlistreverse': opts.playlist_reverse,
    # 'playlistrandom': opts.playlist_random,
    # 'noplaylist': opts.noplaylist,
    'logtostderr': outtmpl == '-',
    # 'consoletitle': opts.consoletitle,
    # 'nopart': opts.nopart,
    # 'updatetime': opts.updatetime,
    # 'writedescription': opts.writedescription,
    # 'writeannotations': opts.writeannotations,
    # 'writeinfojson': opts.writeinfojson,
    # 'writethumbnail': opts.writethumbnail,
    # 'write_all_thumbnails': opts.write_all_thumbnails,
    # 'writesubtitles': opts.writesubtitles,
    # 'writeautomaticsub': opts.writeautomaticsub,
    # 'allsubtitles': opts.allsubtitles,
    # 'listsubtitles': opts.listsubtitles,
    # 'subtitlesformat': opts.subtitlesformat,
    # 'subtitleslangs': opts.subtitleslangs,
    # 'matchtitle': decodeOption(opts.matchtitle),
    # 'rejecttitle': decodeOption(opts.rejecttitle),
    # 'max_downloads': opts.max_downloads,
    # 'prefer_free_formats': opts.prefer_free_formats,
    'verbose': verbose,
    # 'dump_intermediate_pages': opts.dump_intermediate_pages,
    # 'write_pages': opts.write_pages,
    # 'test': opts.test,
    # 'keepvideo': opts.keepvideo,
    # 'min_filesize': opts.min_filesize,
    # 'max_filesize': opts.max_filesize,
    # 'min_views': opts.min_views,
    # 'max_views': opts.max_views,
    # 'daterange': date,
    'cachedir': cachedir,
    # 'youtube_print_sig_code': opts.youtube_print_sig_code,
    # 'age_limit': opts.age_limit,
    # 'cookiefile': opts.cookiefile,
    # 'nocheckcertificate': opts.no_check_certificate,
    # 'prefer_insecure': opts.prefer_insecure,
    # 'proxy': opts.proxy,
    # 'socket_timeout': opts.socket_timeout,
    # 'bidi_workaround': opts.bidi_workaround,
    # 'debug_printtraffic': opts.debug_printtraffic,
    # 'prefer_ffmpeg': opts.prefer_ffmpeg,
    # 'include_ads': opts.include_ads,
    # 'default_search': opts.default_search,
    # 'youtube_include_dash_manifest': opts.youtube_include_dash_manifest,
    # 'encoding': opts.encoding,
    # 'extract_flat': opts.extract_flat,
    # 'mark_watched': opts.mark_watched,
    # 'merge_output_format': opts.merge_output_format,
    # 'postprocessors': postprocessors,
    # 'fixup': opts.fixup,
    # 'source_address': opts.source_address,
    # 'call_home': opts.call_home,
    # 'sleep_interval': opts.sleep_interval,
    # 'max_sleep_interval': opts.max_sleep_interval,
    # 'external_downloader': opts.external_downloader,
    # 'list_thumbnails': opts.list_thumbnails,
    # 'playlist_items': opts.playlist_items,
    # 'xattr_set_filesize': opts.xattr_set_filesize,
    # 'match_filter': match_filter,
    # 'no_color': opts.no_color,
    # 'ffmpeg_location': opts.ffmpeg_location,
    # 'hls_prefer_native': opts.hls_prefer_native,
    # 'hls_use_mpegts': opts.hls_use_mpegts,
    # 'external_downloader_args': external_downloader_args,
    # 'postprocessor_args': postprocessor_args,
    # 'cn_verification_proxy': opts.cn_verification_proxy,
    # 'geo_verification_proxy': opts.geo_verification_proxy,
    # 'config_location': opts.config_location,
    # 'geo_bypass': opts.geo_bypass,
    # 'geo_bypass_country': opts.geo_bypass_country,
    # 'geo_bypass_ip_block': opts.geo_bypass_ip_block,
    # just for deprecation check
    # 'autonumber': opts.autonumber if opts.autonumber is True else None,
    # 'usetitle': opts.usetitle if opts.usetitle is True else None,
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(url_to_download)
    info = ydl.extract_info(url_to_download[0], download=False)
    filename = info.get('title')
    mp4_file = ydl.prepare_filename(info)

    if (alsoAudioFile):
        video = VideoFileClip(mp4_file)
        if not os.path.exists(audioDir):
            os.mkdir(audioDir)
        video.audio.write_audiofile(audioDir + filename + '.mp3')
