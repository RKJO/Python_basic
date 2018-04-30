from time import sleep

while True:
    try:
        print('woohoo')
        sleep(1)
    except BaseException:
        print('exception')