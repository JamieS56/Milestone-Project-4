import datetime
import random


def createRandomPK():
    date_time = datetime.datetime.now().strftime("%d-%Y (%H:%M:%S.%f)")

    charectors_to_remove = ":.() -"

    for charector in charectors_to_remove:
        date_time = date_time.replace(charector, "")

    pk = ''
    pk = str(random.randint(0, 99)) + date_time

    return pk
    