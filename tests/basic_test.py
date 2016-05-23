import os
import sys
import time
import codecs
import rarfile
import zipfile
import tempfile

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../resources/lib")

from TorecSubtitlesDownloader import TorecSubtitlesDownloader

def convert_to_utf(file):
  ''' 
  Convert a file in cp1255 encoding to utf-8
  :param file: file to converted from CP1255 to UTF8
  '''
  try:
    with codecs.open(file,"r","cp1255") as f:
      srtData = f.read()

    with codecs.open(file, 'w', 'utf-8') as output:
      output.write(srtData)
  except UnicodeDecodeError:
    log(__name__, "got unicode decode error with reading subtitle data")

downloader  = TorecSubtitlesDownloader()
search_data = downloader.search("house of cards season 6")
option      = search_data.options[0]
page_id     = search_data.id
subtitle_id = option.id

result                 =  downloader.get_download_link(page_id, subtitle_id, False)
subtitleData, fileName = downloader.download(result)
extension              = os.path.splitext(fileName)[1]

temp = tempfile.NamedTemporaryFile()
temp.write(subtitleData)
temp.flush()

if (extension == ".zip"):
  rf = zipfile.ZipFile(temp.name)
elif (extension == ".rar"):
  rf = rarfile.RarFile(temp.name)
else:
  sys.exit(1)  

for f in rf.infolist():
  data = rf.read(f.filename)

  temp = tempfile.NamedTemporaryFile()
  temp.write(data)
  temp.flush()

  out = convert_to_utf(temp.name)
  print temp.read()
  break
