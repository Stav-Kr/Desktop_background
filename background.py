from os import system as s
from datetime import datetime

sunrise = '06'
noon = '12'
sunset = '17'
night = '20'

time_of_day = datetime.now()
real_time = time_of_day.strftime("%H")

def switch_background(path):
 	s('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "{}"\''.format(path))
    


if real_time > sunrise and real_time < noon:
    switch_background("dawn.jpg")
elif real_time <= sunrise:
    switch_background("night.jpg")
elif real_time >= noon and real_time < sunset:
    switch_background("noon.jpg")
elif real_time >= sunset and real_time < night:
    switch_background("sunset.jpg")