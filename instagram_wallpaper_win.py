import urllib.request
import ctypes
import os

response = urllib.request.urlopen('https://www.instagram.com/ravivora/')
result = response.read().decode('utf-8')

begin = result.find("display_url") + 14
end = result.find("_n.jpg",begin) + 6
image_path=result[begin:end]
fullfilename = os.path.join(os.getcwd(), "wallpaper.jpg")
urllib.request.urlretrieve(image_path, fullfilename)

ctypes.windll.user32.SystemParametersInfoW(20, 0, fullfilename ,3)
