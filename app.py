from adb.client import Client as AdbClient
from time import sleep


def swipe_to_next():
    device.shell('input swipe 500 500 500 173.5')


def back():
    device.shell('input keyevent 4')


def click_job():
    device.shell('input tap 540 580')


def click_contact():
    device.shell('input tap 538 1944')


client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()
for device in devices:
    print('Device %s connected' % device)
    i = 1
    while(True):
        print('Try next job: %s' % i)
        swipe_to_next()
        click_job()
        click_contact()
        back()
        back()
        sleep(0.5)
        i = i + 1
