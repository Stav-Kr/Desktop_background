from os import system as s
from datetime import datetime
from unicodedata import name

sunrise = "06"
noon = "12"
sunset = "17"
night = "20"

time_of_day = datetime.now()
real_time = time_of_day.strftime("%H")


def switch_background(path):
    s(
        'osascript -e \'tell application "System Events" to set picture of every desktop to POSIX file "{}"\''.format(
            path
        )
    )


def switch_on_time():
    if real_time > sunrise and real_time < noon:
        switch_background(
            "dawn.jpg"
        )
    elif real_time <= sunrise:
        switch_background(
            "night.jpg"
        )
    elif real_time >= noon and real_time < sunset:
        switch_background(
            "noon.jpg"
        )
    elif real_time >= sunset and real_time < night:
        switch_background(
            "sunset.jpg"
        )
    elif real_time >= night:
        switch_background(
            "night.jpg"
        )


if __name__ == "__main__":
    switch_on_time()
