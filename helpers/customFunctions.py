import datetime
import random


def createRandomPK():
    """ This creates a random string of numbers that can be used as a primary key."""
    
    date_time = datetime.datetime.now().strftime("%d-%Y (%H:%M:%S.%f)")

    charectors_to_remove = ":.() -"

    for charector in charectors_to_remove:
        date_time = date_time.replace(charector, "")

    pk = ''
    pk = str(random.randint(0, 99)) + date_time

    return pk


def add_no_image(players):
    """ If a player instance has no picture it will be given the no-image picture."""

    try:
        for player in players:
            if player.image_url == '':
                player.image_url = 'no-image.jpg'
    except TypeError:
        if players.image_url == '':
            players.image_url = 'no-image.jpg'

    return players
