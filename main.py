import webbrowser as browser
import urllib.request
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volume.SetMasterVolumeLevel(-0, None)
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
try:
    urllib.request.urlopen("http://google.com")
except:
    print("Failed to Connect")
browser.open(link)