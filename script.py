#import web driver 
import webbrowser as browser

#import audio utilities
from subprocess import call

#cranks the volume to eleven(100)
call(["osascript -e 'set volume output volume 100'"], shell=True)

#opens link
link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
browser.open(link)
